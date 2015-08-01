__author__ = 'uv2sun'

'''
    python中没有
    expr?'ret1':'ret2'
    这样的三元表达式。
    但是可以用if 或者 and or 短路用法一样使用

'''

age = 33

print('you are %s' % (age > 30 and 'still young' or 'young'))
print('you are %s' % ('still young' if age > 30 else 'young'))

a = 0
a = '>30' if age > 30 else '<=30'
print(a)
