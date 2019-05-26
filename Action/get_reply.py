#encoding=utf-8
from Config.PublicData import RESPONSE_DATA,REQUEST_DATA
from Utils.md5_encrypt import md5_Encrypt
from data_store import *
from Utils.ParseExcel import *
from Config.PublicData import *
class GetKey(object):
    def __init__(self):
        pass
    @classmethod
    def get(cls,datasource,relydata):
        data = datasource.copy()
        pse = ParseExcel(file_path)

        datas = []
        data1 = {}
        for key,value in relydata.items():

            if key=="request":
           #从REQUEST_DATA获取值
                for k,v in value.items():
                    if "->" in v:
                        interfaceName,case_id=v.split("->")
                        val=REQUEST_DATA[interfaceName][case_id][k]
                        #return data
                    else:
                        interfaceName = v
                        print "interfaceName:", interfaceName
                        pse.get_sheet_by_index(0)
                        for row in pse.get_all_rows():
                            print "row:", row
                            print row[API_apiName - 1].value
                            if row[API_apiName - 1].value == v:
                                caseName = row[API_apiTestCaseFileName - 1].value
                                print caseName
                                pse.get_sheet_by_name(caseName)

                                caseActiveObj = pse.get_single_col(CASE_active - 1)
                                # for id,col in enumerate(caseResponseData[1:],1):
                                for id, col in enumerate(caseActiveObj[1:], 1):
                                    if col.value == "y":
                                        print "k:", k
                                        print "id:", id
                                        val = REQUEST_DATA[interfaceName][str(id)][k]
                                        print "val:", val
                                        data1[k] = val

                                        if len(datas) == 0:
                                            datas.append(data1)
                                            print len(datas)
                                            data1 = {}
                                        elif len(datas) > 0:
                                            print len(datas)
                                            if datas[len(datas) - 1].has_key(k):
                                                datas.append(data1)
                                                data1 = {}
                                            else:
                                                datas[id - 1][k] = val
                        #return data
                    if k=="password":
                        data[k]=md5_Encrypt(val)
                        #return data
                    else:
                        data[k]=val
                        #return data
            elif key == "response":
                for k, v in value.items():
                    print "k value:", k
                    if "->" in v:
                        interfaceName, case_id = v.split("->")
                        data[k] = RESPONSE_DATA[interfaceName][case_id][k]
                        # return data
                    else:

                        interfaceName = v
                        print "interfaceName:", interfaceName
                        pse.get_sheet_by_index(0)
                        for row in pse.get_all_rows():
                            print "row:", row
                            print row[API_apiName - 1].value
                            if row[API_apiName - 1].value == v:
                                caseName = row[API_apiTestCaseFileName - 1].value
                                print caseName
                                pse.get_sheet_by_name(caseName)

                                caseActiveObj = pse.get_single_col(CASE_active - 1)
                                # for id,col in enumerate(caseResponseData[1:],1):
                                for id, col in enumerate(caseActiveObj[1:], 1):
                                    if col.value == "y":
                                        print "k:", k
                                        print "id:", id
                                        val = RESPONSE_DATA[interfaceName][str(id)][k]
                                        print "val:", val
                                        data1[k]=val

                                        if len(datas)==0:
                                            datas.append(data1)
                                            print len(datas)
                                            data1={}
                                        elif len(datas)>0:
                                            print len(datas)
                                            if datas[len(datas)-1].has_key(k):
                                                datas.append(data1)
                                                data1={}
                                            else:
                                                datas[id-1][k]=val




        if datas:
            return json.dumps(datas)
            #print json.dumps(datas)

        else:
            return data



if __name__ == '__main__':
    datasources = {"username":"","password":""}
    #relydatas = {"request":{"username":"register->1","password":"register->1"}}
    #relydatas={"request": {"userid": "login->1", "token": "login->1", "articleId": "create"}}
    relydatas = {"request": {"userid": "login->1", "token": "login->1"}}
    print GetKey.get(datasources, relydatas)


