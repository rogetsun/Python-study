__author__ = 'uv2sun'

'''
    注意filter返回的是一个iterator
'''
l = filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in l:
    print(i)


