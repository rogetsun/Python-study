__author__ = 'uv2sun'

s = '65:%c, "65":%c' % (65, 65)  # %c不可使用字符串，api解释可以使用字符。。。。

print(s)

s = '%u' % (-255)

print(s)

s = '%E' % (123456)

print(s)

s = '1111'
print(int(s, 2))

print('abc'.isalnum())
print('123'.isalnum())
print('我们'.isalnum())
print(''.isalnum())
s = '123s4'
print(s.isnumeric())
print('123'.isnumeric())
a = ['songyw', 'litx']
print(',,'.join(a))

print('ssssddddffff'.maketrans('s', '1'))

print('%015d' % (1234566,))

print('a1b2c3d4e5f6'[3::2])
