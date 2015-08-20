__author__ = 'uv2sun'

from m1 import m1

print(m1)
func = getattr(m1, 'test_getattr')
func()
