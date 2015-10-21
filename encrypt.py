# coding:utf-8
__author__ = 'uv2sun'

import hashlib

m = hashlib.md5()
m.update("admin".encode('utf-8'))
print(m.digest())
print(m.hexdigest())
