__author__ = 'uv2sun'

import traceback
import sys
import json
#
# try:
#     json.loads()
# except:
#     traceback.print_exc()
#     print('****错误位置打印在本打印之后？不准确****')
#
# try:
#     json.loads()
# except Exception as e:
#     print(Exception, ':', e)
#     print('****异常类是Exception，最好是TypeError****')
#
try:
    json.loads()
except:
    e_info = sys.exc_info()
    print(e_info[0], '======', e_info[1])
    print('****最准确****')
