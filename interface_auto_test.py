#encoding=utf-8
import requests
import json
from Utils.ParseExcel import *
from Utils.HttpClient import *
from Config.PublicData import *
from Action.data_store import *
from Action.check_result import *
from Action.get_reply import *
from Action.write_test_result import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main(file_path):
    pse=ParseExcel(file_path)
    pse.get_sheet_by_index(0)
    activeList = pse.get_single_col(API_active-1)
    #  enumerate(activeList,2) 中的2 表示从idx索引从2开始
    for idx, cell in enumerate(activeList[1:],1):
        if cell.value=="y":
            pse.get_sheet_by_index(0)
            rowObj = pse.get_single_row(idx)
            apiName = rowObj[API_apiName-1].value
            requestUrl = rowObj[API_requestUrl - 1].value
            requestMethod = rowObj[API_requestMothod - 1].value
            paramsType = rowObj[API_paramsType - 1].value
            apiTestCaseFileName = rowObj[API_apiTestCaseFileName - 1].value
            pse.get_sheet_by_name(apiTestCaseFileName)
            caseActiveObj=pse.get_single_col(CASE_active-1)
            for c_idx,col in enumerate(caseActiveObj[1:],1):
                if col.value=="y":
                    caseRowObj = pse.get_single_row(c_idx)
                    requestData = caseRowObj[CASE_requestData - 1].value
                    print requestData
                    relyData = caseRowObj[CASE_relyData - 1].value
                    dataStore = caseRowObj[CASE_dataStore - 1].value
                    checkPoint = caseRowObj[CASE_checkPoint - 1].value
                    if relyData:
                        requestData="%s"%GetKey.get(eval(requestData),eval(relyData))
                    httpC = HttpClient()
                    response = httpC.request(requestMethod=requestMethod,requestUrl=requestUrl,paramType=paramsType,requestData=requestData)
                    pse.write_cell_content(row_no=c_idx + 1, col_no=CASE_responseCode, content=response.status_code)
                    """
                    if response.status_code == 200:
                        responseData=response.json()
                        if dataStore:
                            RelyDataStore.do(eval(dataStore),apiName,c_idx,eval(requestData),responseData)
                        errorKey= CheckResult.check(responseData,eval(checkPoint))
                        write_result(pse,responseData,errorKey,c_idx)
                    else:
                        print response.status_code
                    """
                    responseData = response.json()
                    if dataStore:
                        RelyDataStore.do(eval(dataStore), apiName, c_idx, eval(requestData), responseData)
                    errorKey = CheckResult.check(responseData, eval(checkPoint))
                    write_result(pse, responseData, errorKey, c_idx)
                else:
                    print "用例被忽略执行"
        else:
            print "接口被设置忽略执行"
if __name__=="__main__":
    main("e:\\test\\Interfaces\\TestData\\inter_test_data.xlsx")






        




