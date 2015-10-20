__author__ = 'uv2sun'

a = 'sss'
print(1 and a)

print('abc {0} , {1}'.format('xx', 'abc'))

print('abc %s, %s' % ('xx', 'abc'))

p = ['a', 'b', 'c', 'd']
s = [1, 2, 4, 5]
ps = dict(zip(p, s))

print(ps)

for k, v in ps.items():
    print(k, v)

print(ps.setdefault('d', 'xxxx'))
print(ps)
print(ps.setdefault('e', 'eeee'))

print(ps)
print(isinstance(ps, dict))

L = [
    i * 100 + j * 10 + n
    for i in range(1, 10)
    for j in range(0, 10)
    for n in range(1, 10)
    if i == n and i != j
    ]

print(L)


def formats(x):
    return x[0:1].upper() + x[1:].lower()


str = map(formats, ['LITX', 'songyw'])
print(str)
for i in str:
    print(i)


def reFormats(a, b):
    return a + b


print(reFormats.__name__)

from functools import reduce

str = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(str)

l = filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in l:
    print(i)


def add(a, b, c):
    return a + b + c


import functools

add2 = functools.partial(add, b=3, c=2)
print(add2(12))

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(10000 * 60 * 60)))

print(24 * 30 * 14)




x = 10
if x > 10:
    ret = '>10'
else:
    ret = "<10"

print(ret)
