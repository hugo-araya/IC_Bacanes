cont = 0
suma = 0
cantidad = int(input('Cantidad de notas: '))
while cont < cantidad:
    nota = float(input('Nota '+str(cont + 1)+': '))
    if nota >= 1 and nota <= 7:
        suma = suma + nota
        cont = cont + 1
    else:
        print('Nota fuera de rango, reingrese.')





promedio = suma / cantidad
if promedio >= 4:
    print('Promedio: ', promedio, ' Se salvo ....')
else:
    print('Promedio ', promedio, 'RIP')


