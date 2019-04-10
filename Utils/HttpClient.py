#encoding=utf-8
import requests
import json

class HttpClient(object):
    def __init__(self):
        pass
    def request(self,requestMethod,requestUrl,paramType,requestData=None,headers=None,cookies=None):
        if requestMethod.lower()=="post":
            if paramType=="form":
                response = self.__post(url=requestUrl,data=json.dumps(eval(requestData)),headers=headers,cookies=cookies)
                return response
            elif paramType=="json":
                response =  self.__post(url=requestUrl,json=json.dumps(eval(requestData)),headers=headers,cookies=cookies)
                return response
        elif requestMethod.lower()=="get":
            if paramType=="url":
                request_Url="%s%s",(requestUrl,requestData)
                response = self.__get(url = request_Url,headers=headers,cookies=cookies)
                return response
            elif paramType=="params":
                response=self.__get(url=requestUrl,params=requestData,headers=headers,cookies=cookies)
                return response
    def __post(self,url,data=None,json=None,**kwargs):
        response = requests.post(url=url,data=data,json=json)
        return response

    def __get(self,url,params=None,**kwargs):
        response = requests.get(url=url,params=params)
        return response

if __name__=="__main__":
    hc = HttpClient()
    res = hc.request("post","http://39.106.41.11:8080/register/","form",'{"username":"lilysdd12","password":"lily12323","email":"lily@qq.com"}')
    #列出所有res的参数
    print (dir(res))

            

