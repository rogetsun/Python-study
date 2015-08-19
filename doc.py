__author__ = 'uv2sun'


def test_doc(doc):
    """ 测试函数文档 """
    print(doc)


test_doc('a')

print(test_doc.__doc__)
