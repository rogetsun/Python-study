__author__ = 'uv2sun'

import time
import datetime

t = time.time() * 1000  # 毫秒级别
print(t)
timestamp = int(t)
print(timestamp)

print(1024 * 8 / 7)

import json

j = json.loads('{"a":1, "b":2}')
print(j)
print('len=%s' % len(j))
print('type=%s' % type(j))
print(j['a'])

s = json.dumps(j)
print(s)

print(type(s))
print(len(s))
