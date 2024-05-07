frase1 = 'Hasta ahora la entidad ha entregado una serie de antecedentes que dan cuenta de como se habria iniciado el acuerdo y a quienes habria afectado'
frase2 = 'Los productos afectados por esta colusion son sumamente relevantes para el funcionamiento de multiples areas de nuestra economia y la salud de las personas'
lista1 = frase1.split(' ')
lista2 = frase2.split(' ')

lista3 = lista1 + lista2
lista33 = []
for palabra in lista3:
    if palabra not in lista33:
        lista33.append(palabra)

lista4 = []
for palabra in lista1:
    if palabra in lista2:
        lista4.append(palabra)
print(lista4)

lista44 = []
for palabra in lista4:
    if palabra not in lista44:
        lista44.append(palabra)
print(lista44)


