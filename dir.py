__author__ = 'uv2sun'
import sys
import reduce as max2
# eval('import reduce')
# from reduce import max

try:
    def mydir(m):
        dic = dir(m)
        arr = []
        for a in dic:
            if a[0] is not '_':
                # print('add %s' % a)
                arr.append(a)
        return arr


    def test():
        print(mydir(max2))
        ms = mydir(max2)
        print(len(ms))
        # for i in ms:
        #     print(i)
except:
    info = sys.exc_info()
    print(info[0], '---------', info[1])

# print(dir())
