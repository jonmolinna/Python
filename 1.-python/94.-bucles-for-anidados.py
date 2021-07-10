# Reto 1
# Crea una baraja con bucles añadiendo las cartas a una lista mediante bucles for

tantos = ["A", "2", "3", "4", "5", "6", "7", "8", "S", "C", "R"]
palos = ["oros", "copas", "espadas", "bastos"]
barajas = []

for tanto in tantos:
    for palo in palos:
        barajas.append(f"{tanto} de {palo}")

for baraja in barajas:
    print(baraja)


# Reto 2
# Programa tablas de multiplicar del 2 al 7

for i in range(1, 11):
    for m in range(2, 8):
        #print(f"{i} X {m} = {i * m}")
        print("{:2} X {:2} = {:2}   ".format(m,i,m*i), end="")
    print()

# Reto 3
# Programa que muestra todas las posibles combinaciones para poder abrir un candado de clave de tres ruedas

for i in range(10):
    for j in range(10):
        for k in range(10):
            combinaciones = str(i) + str(j) + str(k)
            print(combinaciones)

# Reto 4
# Cinco amigos van a hacer una carrera: "Tomas", "Maria", "Laura", "Miguel", "Carlos"
# Muestra todos los posibles resultados que se pueden dar en esa carrera. Es decir, el orden en que pueden llegar
# a la meta los cinco amigos, Incluye un contador que compruebe cuantas posibilidades se dan
# Permutacion sin repeticion de 5 elementos formular => m!

amigos = ["Tomas", "Maria", "Laura", "Miguel", "Carlos"]
contador = 0

for i in amigos:
    for j in amigos:
        for k in amigos:
            for m in amigos:
                for n in amigos:
                    if i != j and i != k and i != m and i != n and \
                        j != k and j != m and j != n and \
                        k != m and k != n and m != n:
                        orden = [i, j, k, m, n]
                        contador += 1
                        print("{:3d} : {}".format(contador, orden))


# Reto 5
# Para un juego que va a tener 20.000 planetas necesitamos formar nombres para cada uno de ellos.
# Crea una lista con todos los nombres de 3 silabas que se pueden formar 10 consonantes y 5 vocales,
# de tal forma que se intercambien consonantes y vocal, y no se repita ninguna letra en cada nombre.
# Al final muestra la cantidad de nombres de la lista y muestra 10 al azar

import random

consonantes = "bdklnprstz"
vocales = "aeiou"
nombres = []

for c1 in consonantes:
    for v1 in vocales:
        for c2 in consonantes:
            for v2 in vocales:
                for c3 in consonantes:
                    for v3 in vocales:
                        if c1 != c2 and c1 != c3 and c2 != c3 and \
                            v1 != v2 and v1 != v3 and v2 != v3:
                            nombre = c1 + v1 + c2 + v2 + c3 + v3
                            nombres.append(nombre)

print("Cantidad de Nombres: {}".format(len(nombres)))

for i in range(1,11):
    planeta = random.choice(nombres)
    print("Planeta {} : {}".format(i, planeta))


# Reto 6
# En una leteria hay un bombo que tiene 10 bolas, con los numeros del 1 al 10
# En un sorteo se sacan 5 bolas, sin que se introduzcan las bolas en que se han sacado previamente, Haz
# un programa que muestre todas las apuestas posibles, es decir, todas las combinaciones posibles que se pueden
# dar en esa loteria incluye un contador para comprobar el numero de combinaciones que se dan
# Hay 10 elementos y se toman de 5 en 5 no se pueden repetir. EL orden no importa.

combinaciones = []
contador = 0

for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            for m in range(1,11):
                for n in range(1,11):
                    if i != j and i != k and i != m and i != n and \
                        j != k and j != m and j != n and \
                        k != m and k != n and m != n:
                        comb = [i, j, k, m, n]
                        comb.sort()
                        if comb not in combinaciones:
                            combinaciones.append(comb)
                            contador += 1
                            print("{:3} : {}".format(contador, comb))


# Reto 7
# Programa que adivina una clave mediante fuerza bruta.
# La clave consiste en 4 letras minusculas
# La clave puede tener entre 1 y 5 caracteres

import time

clave = input("Dime una clave: ")
alfabeto = " qwertyuiopasdfghjklñ<zxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890"
intento = None
inicio = time.time()

for c1 in alfabeto:
    if intento != clave:
        for c2 in alfabeto:
            if intento != clave:
                for c3 in alfabeto:
                    if intento != clave:
                        for c4 in alfabeto:
                            if intento != clave:
                                for c5 in alfabeto:
                                    cc = c1 + c2 + c3 + c4 + c5
                                    intento = cc.strip()
                                    if intento == clave:
                                        print("Clave econtrada: ", intento)
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
    else:
        break
                

final = time.time()
print("Tiempo consumido: {:5.2f}".format(final - inicio))


# Reto 8
# Encontrar los numeros repetidos de una lista

numeros = [2, 3, 5, 1, 4, 3, 6, 7, 9, 5, 8]
repetidos = []

for i in range(len(numeros)):
    for j in range(len(numeros)):
        if i != j:
            if numeros[i] == numeros[j] and numeros[i] not in repetidos:
                repetidos.append(numeros[i])

print(repetidos)

# Otra forma de Hacer

numeros = [2, 3, 5, 1, 4, 3, 6, 7, 9, 5, 8]
repetidos = []
archivo = []

for n in numeros:
    if n not in archivo:
        archivo.append(n)
    else:
        repetidos.append(n)

print(repetidos)
print(archivo)


# Reto 9
# Comprobar si la suma de dos numeros de una lista dan como resultado 10, y mostrar todas las soluciones.
# (No cuenta la suma de un numero consigo mismo)

numeros = [2, 3, 5, 8, 4, 7, 6, 5, 1]
parejas = []

for i in range(len(numeros)):
    for j in range(len(numeros)):
        if i != j:
            if numeros[i] + numeros[j] == 10:
                pareja = sorted([numeros[i], numeros[j]])
                if pareja not in parejas:
                    parejas.append(pareja)

print(parejas)

# Otra forma

for n in numeros:
    copia = list(numeros)
    copia.remove(n)
    if 10 - n in numeros:
        pareja = sorted([n, 10-n])
        if pareja not in parejas:
            parejas.append(pareja)

print(parejas)