__author__ = 'uv2sun'

out = 'i am out'

print(out)


def changeout():
    global out
    out = 'i am out but change in func'


changeout()
print(out)


def outer():
    out = 'i am outer'
    print(out)

    def inner():
        global out  # 此处out为全局变量out = 'i am out'
        # nonlocal out  # 此处out为函数outer()内部的out = 'i am outer'
        #上面两者不能同时修饰同名的变量
        out = 'xxxxx'

    inner()
    print(out)

outer()
print(out)
