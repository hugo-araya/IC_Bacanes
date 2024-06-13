def lee_archivo(nombre):
    ent = open(nombre)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split()
        datos.append(lista)
    ent.close()
    return datos

def calcula_promedio(year, datos):
    suma = 0
    cantidad = 0
    for dato in datos:
        fecha = dato[0].split('-')
        if int(fecha[2]) == year:
            suma = suma + float(dato[1])
            cantidad = cantidad + 1
    prom = suma / cantidad
    return prom

def funcion_1(datos):
    promedios = []
    year = 2013
    while year < 2020:
        prom_year = calcula_promedio(year,datos)
        promedios.append([year, prom_year])
        year = year + 1
    return promedios

def calcula_minimo(datos):
    minimo = 2000
    for dato in datos:
        if float(dato[1]) < minimo:
            minimo = float(dato[1])
            fecha = dato[0]
    return [fecha, minimo]

def calcula_maximo(datos):
    maximo = 0
    for dato in datos:
        if float(dato[1]) > maximo:
            maximo = float(dato[1])
            fecha = dato[0]
    return [fecha, maximo]

def funcion_2(datos):
    for dato in datos:
        mini = calcula_minimo(datos)
        maxi = calcula_maximo(datos)
    return mini, maxi

def genera_salida(promedios, mini, maxi):
    sal = open('resumen.txt', 'w')
    for promedio in promedios:
        sal.write("Promedio "+str(promedio[0])+": "+str(promedio[1])+'\n')
    fecha_max = maxi[0].split('-')
    fecha_min = mini[0].split('-')
    sal.write('El mayor valor corresponde al dia '+fecha_max[0]+' del mes '+fecha_max[1]+' de '+fecha_max[2]+'\n')
    sal.write('El mayor valor corresponde al dia '+fecha_min[0]+' del mes '+fecha_min[1]+' de '+fecha_min[2]+'\n')
    sal.close()

if __name__ == '__main__':
    datos = lee_archivo('datos.txt')
    promedios = funcion_1(datos)
    mini, maxi = funcion_2(datos)
    genera_salida(promedios, mini, maxi)