#encoding=utf-8
from Config.PublicData import RESPONSE_DATA,REQUEST_DATA
from Utils.md5_encrypt import md5_Encrypt
from data_store import *
class GetKey(object):
    def __init__(self):
        pass
    @classmethod
    def get(cls,datasource,relydata):
        data = datasource.copy()
        for key,value in relydata.items():
            if key=="request":
           #从REQUEST_DATA获取值
                for k,v in value.items():
                    interfaceName,case_id=v.split("->")
                    val=REQUEST_DATA[interfaceName][case_id][k]
                    if k=="password":
                        data[k]=md5_Encrypt(val)
                    else:
                        data[k]=val

            elif key=="response":
                for k,v in value.items():
                    interfaceName,case_id=v.split("->")
                    data[k] = RESPONSE_DATA[interfaceName][case_id][k]
        return data
if __name__ == '__main__':
    datasources = {"username":"","password":""}
    relydatas = {"request":{"username":"register->1","password":"register->1"}}
    print GetKey.get(datasources, relydatas)

