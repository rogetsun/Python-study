# coding:utf-8
__author__ = 'uv2sun'


'''
注意:
    3.*版本中filter返回的是一个iterator
    2.*版本中返回list
'''
l = filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(l)
for i in l:
    print(i)
