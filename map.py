__author__ = 'uv2sun'


def formats(x):
    return x[0:1].upper() + x[1:].lower()


'''
    注意map函数返回的是iterator
'''
str = map(formats, ['LITX', 'songyw'])
print(str)
for i in str:
    print(i)

l = map(lambda x, y, z: x + y + z, [1, 2, 3], [1, 2, 3], [1, 2, 3])
print(type(l))
l = [i for i in l]
print(l)
