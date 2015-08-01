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