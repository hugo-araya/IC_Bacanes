nombre1 = input('Nombre 1 : ')
nombre1 = nombre1.upper()
nombre2 = input('Nombre 2 : ')
nombre2 = nombre2.upper()
if (nombre1[0] == nombre2[0]) or (nombre1[-1] == nombre2[-1]):
    print('True')
else:
    print('False')