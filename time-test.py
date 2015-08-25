__author__ = 'uv2sun'

import time
import datetime

t = time.time() * 1000  # 毫秒级别
print(t)
timestamp = int(t)
print(timestamp)

print(1024 * 8 / 7)

dt = datetime.datetime.now()
print(dt)

t = time.localtime(2 ** 32)  # this is the max datetime in unix windows now
print(time.strftime('%Y-%m-%d %H:%M:%S', t))
