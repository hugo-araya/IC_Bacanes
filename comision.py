# Entero sueldo_base, venta1, venta2, venta3
# Entero total_venta
# Real comision, sueldo_recibir
SALTO = '\n'
sueldo_base = int(input('Sueldo base: '))  
interes = float(input('Interes: ')) 
venta1 = int(input('Venta 1: '))
venta2 = int(input('Venta 2: '))
venta3 = int(input('Venta 3: '))
total_venta = venta1 + venta2 + venta3
comision = total_venta * interes / 100
sueldo_recibir = sueldo_base + comision
salida1 = 'Sueldo a recibir $'+ str(sueldo_recibir)
salida2 = 'Comision a recibir $'+str(comision)
print(salida1, end='')
print(SALTO*2, end = '')
print(salida2)
