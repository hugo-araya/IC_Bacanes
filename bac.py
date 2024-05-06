abc = list('abcdefghijklmnopqrstuvwxyz')
i = 0
while i < len(abc):
    abc[i] = '*'
    i = i + 3
contar = abc.count('*')
i = 0
while i < contar:
    abc.remove('*')
    i += 1
print(abc)


print(abc)