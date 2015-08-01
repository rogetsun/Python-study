__author__ = 'uv2sun'

'''
匿名函数定义语法：
    lambda 入参 : 返回值表达式
'''


def func1(func, list):
    temp = list[0]
    for i in range(1, len(list)):
        temp = func(temp, list[i])
    return temp


arr = [4, 5, 6]
lb = (9, 2, 3)

'''
这里 lambda a, b: a + b
为一个匿名函数，
    入参2个： a, b
    返回值： a+b
'''
t = func1(lambda a, b: a + b, lb)

print(t)

print('test 2: 直接调用')
(lambda a: print(a) )('fdsfdsfdsfdfds')