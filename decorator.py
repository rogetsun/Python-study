# coding:utf-8
__author__ = 'uv2sun'
import functools


def decorator1(func):
    """不包含参数的装饰器"""
    print('装饰器[%s]函数开始装饰' % decorator1.__name__)

    @functools.wraps(func)
    def wapper(*args, **kwargs):
        print('[%s]装饰操作:' % decorator1.__name__),
        print(args)
        print(kwargs)
        return func(*args, **kwargs)

    return wapper


def decorator2(name):
    """带参数的装饰器，decorator2用于接收装饰器函数，并返回真正的装饰器函数"""
    print('[%s]接收装饰器参数，生成装饰器函数' % decorator2.__name__)

    def decorator_fn(func):
        """真正用来装饰的函数"""
        print('[%s][%s]装饰器函数开始装饰' % (decorator2.__name__, name))

        @functools.wraps(func)
        def wapper(*args, **kwargs):
            """装饰后，真正用户执行的函数"""
            print('[%s][%s]装饰操作:' % (decorator2.__name__, name)),
            print(args),
            print(kwargs)
            return func(*args, **kwargs)

        return wapper

    return decorator_fn


@decorator1
def test_f1(param):
    print('函数[%s]参数是：%s' % (test_f1.__name__, param))


@decorator2(name='songyw')
def test_f2(param):
    print('函数[%s]参数是：%s' % (test_f1.__name__, param))


test_f1('litx')
test_f2('litx')
