__author__ = 'uv2sun'


def add(a, b) -> 'test':
    print(add.__annotations__)

    def inner():
        print(inner.__closure__)

    inner()
    return a + b


from functools import reduce


def max(list):
    sum = reduce(lambda x, y: (x > y and x or y), list)
    return sum


print(max([10, 10, 10, 20, 20, 20, 33, 44]))

# print(add('三角形的树', '北极'))
