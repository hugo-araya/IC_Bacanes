abc = list('abcdefghijklmnopqrstuvwxyz')
i = 0
borrar = []
while i < len(abc):
    borrar.append(abc[i])
    i = i + 3
i = 0
while i < len(borrar):
    abc.remove(borrar[i])
    i += 1
print(abc)
