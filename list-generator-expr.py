__author__ = 'uv2sun'

L = [
    i * 100 + j * 10 + n
    for i in range(1, 10)
    for j in range(0, 10)
    for n in range(1, 10)
    if i == n and i != j
    ]

print(L)

ll = []
for i in range(1, 10):
    for j in range(0, 10):
        for n in range(1, 10):
            if i == n and i != j:
                ll.append(i * 100 + j * 10 + n)

print(ll)

json = [
    {'id': 1, 'name': 'n1'},
    {'id': 2, 'name': 'n2'},
    {'id': 3, 'name': 'n3'}
]

print('%s' % (u.get('id') for u in json))
