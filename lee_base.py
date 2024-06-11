ent = open('titanic3_1.txt')
mini = 14
mayo = 14
for linea in ent:
    linea = linea.rstrip('\n')
    lista = linea.split(',')
    if len(lista) > mayo:
        mayo = len(lista)
    if len(lista) < mini:
        mini = len(lista)
print(mini, mayo)
ent.close()
