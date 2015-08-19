__author__ = 'uv2sun'

import time
import datetime

print(time.localtime())
print(datetime.datetime.now())

from myapp import fapp
import sys
print(sys.path)


if __name__ == '__main__':
    fapp.run()

