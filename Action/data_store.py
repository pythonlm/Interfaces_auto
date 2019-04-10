#encoding=utf-8
from Config.PublicData import REQUEST_DATA,RESPONSE_DATA
class RelyDataStore(object):
    def __init__(self):
        pass
    @classmethod
    def do(cls,storePoint,apiName,caseId,request_source={},response_source={}):
         for key,value in storePoint.items():
             # 说明存储的数据来自请求参数
             if key=="request":
                 for i in value:
                      #print i
                      if request_source.has_key(i):
                          if not REQUEST_DATA.has_key(apiName):
                              # 说明存储数据的结构还未生成，需要指明数据存储结构
                              REQUEST_DATA[apiName]={str(caseId):{i:request_source[i]}}
                              #print REQUEST_DATA[apiName]
                          else:
                              # 说明存储数据结构中最外层结构完整
                              if REQUEST_DATA[apiName].has_key(str(caseId)):
                                  REQUEST_DATA[apiName][str(caseId)][i]=request_source[i]
                                  #print REQUEST_DATA[apiName][str(caseId)][i]
                              else:
                                  REQUEST_DATA[apiName][str(caseId)]={i:request_source[i]}
                      else:
                          print u"请求参数中不存在字段："+i

             elif key=="response":
                 # 说明存储的数据来自响应body
                 for j in value:
                     #print j
                     if response_source.has_key(j):
                         if not RESPONSE_DATA.has_key(apiName):
                             # 说明存储数据的结构还未生成，需要指明数据存储结构
                             RESPONSE_DATA[apiName]={str(caseId):{j:response_source[j]}}
                         else:
                             # 说明存储数据结构中最外层结构完整
                             if RESPONSE_DATA[apiName].has_key(str(caseId)):
                                 RESPONSE_DATA[apiName][str(caseId)][j]=response_source[j]
                             else:
                                 RESPONSE_DATA[apiName][str(caseId)]={j:response_source[j]}
                     else:
                         print "响应body中不存在字段" + j
         #print REQUEST_DATA
         #print RESPONSE_DATA


         #return  REQUEST_DATA,RESPONSE_DATA

if __name__ == '__main__':
    request_source = {"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}
    storePoint = {"request":["username","password"],"response":["userid"]}
    response_source = {"userid":12,"code":"00"}
    RelyDataStore.do( storePoint, "register", 1,request_source, response_source)
    print REQUEST_DATA
    print RESPONSE_DATA
    #{'register': {'1': {'username': 'srwcx01', 'password': 'wcx123wac1'}}}
#{'register': {'1': {'userid': 12}}}