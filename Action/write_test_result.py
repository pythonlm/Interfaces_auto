#encoding=utf-8
from Config.PublicData import *
from Utils.ParseExcel import *
def write_result(wbobj,responseData,errorKey,rowNum):
     try:
         #行号和列号从1开始
         wbobj.write_cell_content(row_no=rowNum+1,col_no=CASE_responseData,content="%s"%responseData)
         if errorKey:
             wbobj.write_cell_content(row_no=rowNum+1,col_no=CASE_status,content="fail")
             wbobj.write_cell_content(row_no=rowNum+1,col_no=CASE_errorInfo,content="%s"%errorKey)
         else:
             wbobj.write_cell_content(row_no=rowNum+1,col_no=CASE_status, content="pass")
     except Exception,e:
         raise e
