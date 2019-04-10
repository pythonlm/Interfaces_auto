#encoding=utf-8
import hashlib

def md5_Encrypt(text):
    m5 = hashlib.md5()
    m5.update(text)
    value = m5.hexdigest()
    return value

#print md5_Encrypt('abc123')
