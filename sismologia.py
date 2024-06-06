import matplotlib.pyplot as plt

def lee_datos(nombre):
    datos = []
    ent = open(nombre)
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split()
        datos.append(lista)
    ent.close()
    return datos

def a_funcion(datos):
    mayor = 0
    for lista in datos:
        if float(lista[4]) > mayor:
            mayor = float(lista[4])
            fecha = lista[0]
            hora = lista[1]
    return [fecha, hora]

def b_funcion(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 7 and float(lista[4]) < 8:
            contador = contador + 1
    return contador

def c_funcion(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 8 and float(lista[4]) < 9:
            contador = contador + 1
    return contador

def d_funcion(datos):
    contador = 0
    for lista in datos:
        if float(lista[4]) >= 9:
            contador = contador + 1
    return contador

def e_16_funcion(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0].split('/')
        if int(fecha[2]) < 1600:
            contador = contador + 1
    return contador

def e_17_funcion(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0].split('/')
        if int(fecha[2]) >= 1600 and int(fecha[2]) < 1700:
            contador = contador + 1
    return contador

def e_18_funcion(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0].split('/')
        if int(fecha[2]) >= 1700 and int(fecha[2]) < 1800:
            contador = contador + 1
    return contador

def e_19_funcion(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0].split('/')
        if int(fecha[2]) >= 1800 and int(fecha[2]) < 1900:
            contador = contador + 1
    return contador

def e_20_funcion(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0].split('/')
        if int(fecha[2]) >= 1900 and int(fecha[2]) < 2000:
            contador = contador + 1
    return contador

def e_21_funcion(datos):
    contador = 0
    for lista in datos:
        fecha = lista[0].split('/')
        if int(fecha[2]) >= 2000 and int(fecha[2]) < 2100:
            contador = contador + 1
    return contador

def muestra_salida(res_a, res_b, res_c, res_d, res_e_16, res_e_17, res_e_18, res_e_19, res_e_20, res_e_21):
    print("Fecha:", res_a[0], "y hora:", res_a[1], "del mayor sismo registrado.\n")
    print("Cantidad de sismos >= 7.0 y < 8.0:", res_b,'\n')
    print("Cantidad de sismos >= 8.0 y < 9.0:", res_c,'\n')
    print("Cantidad de sismos >= 9.0:", res_d,'\n')
    print("Cantidad de sismos siglo 16:", res_e_16,'\n')
    print("Cantidad de sismos siglo 17:", res_e_17,'\n')
    print("Cantidad de sismos siglo 18:", res_e_18,'\n')
    print("Cantidad de sismos siglo 19:", res_e_19,'\n')
    print("Cantidad de sismos siglo 20:", res_e_20,'\n')
    print("Cantidad de sismos siglo 21:", res_e_21,'\n')

def grafica(res_e_16, res_e_17, res_e_18, res_e_19, res_e_20, res_e_21):
    x = [16,17,18,19,20,21]
    y = [res_e_16, res_e_17, res_e_18, res_e_19, res_e_20, res_e_21] 
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    datos = lee_datos('terr.txt')
    res_a = a_funcion(datos)
    res_b = b_funcion(datos)
    res_c = c_funcion(datos)
    res_d = d_funcion(datos)
    res_e_16 = e_16_funcion(datos)
    res_e_17 = e_17_funcion(datos)
    res_e_18 = e_18_funcion(datos)
    res_e_19 = e_19_funcion(datos)
    res_e_20 = e_20_funcion(datos)
    res_e_21 = e_21_funcion(datos)
    muestra_salida(res_a, res_b, res_c, res_d, res_e_16, res_e_17, res_e_18, res_e_19, res_e_20, res_e_21)
    grafica(res_e_16, res_e_17, res_e_18, res_e_19, res_e_20, res_e_21)