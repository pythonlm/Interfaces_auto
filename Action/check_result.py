#encoding=utf-8
import re
class CheckResult(object):
    def __init__(self):
        pass
    @classmethod
    def check(cls,responseobj,checkpoint):
        errorkey={}
        for key,value in checkpoint.items():
            if isinstance(value,(str,unicode)):
                if responseobj[key]!=value:
                    errorkey[key]=responseobj[key]
            elif isinstance(value,dict):
                sourcedata = responseobj[key]
                if value.has_key("value"):
                    regStr = value["value"]
                    rg = re.match(regStr,"%s"%sourcedata).group()
                    if not rg:
                        errorkey[key]=sourcedata
                elif value.has_key("type"):
                    types = value["type"]
                    if types=="N":
                        if not isinstance(sourcedata,(int,long)):
                            errorkey[key]=sourcedata
        return errorkey

if __name__ == '__main__':
    responseobj = {"code":"01", "userid":12, "id":"12"}
    checkpoint = {"code": "00", "userid":{"type":"N"}, "id":{"value":"\d+"}}
    print CheckResult.check(responseobj, checkpoint)