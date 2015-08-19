__author__ = 'uv2sun'

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
try:
    print(json.loads())
except Exception as e:
    print(Exception, ':', e)
