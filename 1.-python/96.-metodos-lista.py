# Reto 1
# Mostrar mensaje de presentacion
# Mostrar menu de opciones: Pedir que se elija una opcion.
#   Añadir producto, eliminar producto, mostrar lista, salir.
# Opcion "Añadir producto", pedir nombre del producto.
#   Si ya esta en la lista indicarlo, sino añadirlo.
# Opcion "Eliminar Pruducto", pedir el nombre del producto
#   si no esta indicarlo, sino eliminarlo
# Opcion "Mostrar lista", Mostrar lista
# Opcion "Salir", salir del programa
# Opcion incorrecta: Indicarlo
# Tras cada accion volver al menu: Hasta que se elija "Salir"

compra = []

print("-------------------------------")
print("--- Lista de la Compra --------")
print("-------------------------------")
print()

while True:
    print("1. Añadir producto.")
    print("2. Eliminar producto.")
    print("3. Mostrar lista compra")
    print("4. Salir del Programa")
    print()
    opcion = input("----> ")
    print()

    if opcion == "1":
        producto = input("Introduce el producto: ").capitalize()
        if producto in compra:
            print("Ese producto esta en la lista")
        else:
            compra.append(producto)
    elif opcion == "2":
        producto = input("Introduce el producto: ").capitalize()
        if producto not in compra:
            print("Ese producto no esta en la lista")
        else:
            compra.remove(producto)
    elif opcion == "3":
        print("Lista Compra")
        for e in compra:
            print(" -", e)
    elif opcion == "4":
        break
    else:
        print("Introduce una opcion correcta")


# Reto 2
# Programa que elimina todos los meses que tengan la letra "b"

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

copia_meses = list(meses)

for mes in copia_meses:
    if "b" in mes:
        meses.remove(mes)

print(meses)


# Reto 3
# Programa que borra los elementos repetidos de una lista, y quedan solo elementos unicos, no repetidos

numeros = [1, 2, 3, 2, 5, 3, 4, 6, 5, 7, 8]
number = []

for i in range(len(numeros) - 1, -1, -1):
    if numeros[i] not in number:
        number.append(numeros[i])

print(number)

# Otra forma
numeros = [1, 2, 3, 2, 5, 3, 4, 6, 5, 7, 8]
unicos = []

for i in range(len(numeros) - 1, -1, -1):
    if numeros[i] not in unicos:
        unicos.append(numeros[i])
    else:
        numeros.remove(numeros[i])

print(numeros)
print(unicos)

# Reto 4
# Programa que informa del numero de datos que se han recogido. Pide el numero de datos que se matienen, y
# deja esos datos empezando por los primeros, y borra el resto.
# (Utilizar la sentencia "del")

datos = [1.12, 2.18, 1.45, 2.21, 3.07, 2.32, 3.41, 1.39]

print("Se han recogido", len(datos), "datos.")
n = int(input("Datos que se mantienen: "))
del datos[n:]

print("Los datos son: ")
for i in range(len(datos)):
    print("-", datos[i])


# Reto 5
# Encuentra el numero mayor y el menor de una lista. (La lista puede contener numeros enteros
# positivos y negativos)

numeros1 = [29, 37, 41, 7, 25, 18, 11, 12, 42, 21]
numeros2 = [-23, 27, -16, 11, 32, -35, 48, 6, -1, 17]
numeros3 = [-15, -7, -22, -37, -2, -28, -5, -19, -12, -21]

my1 = numeros1[0]
mr1 = numeros1[0]

for num in numeros1:
    if num > my1:
        my1 = num
    if num < mr1:
        mr1 = num

print(my1, mr1)

my2 = numeros2[0]
mr2 = numeros2[0]
for num in numeros2:
    if num > my2:
        my2 = num
    if num < mr2:
        mr2 = num

print(my2, mr2)

my3 = numeros3[0]
mr3 = numeros3[0]
for num in numeros3:
    if num > my3:
        my3 = num
    if num < mr3:
        mr3 = num

print(my3, mr3)


# Otra forma de hacer 
mayor1 = max(numeros1)
menor1 = min(numeros1)

print(mayor1, menor1)

mayor2 = max(numeros2)
menor2 = min(numeros2)

print(mayor2, menor2)

mayor3 = max(numeros3)
menor3 = min(numeros3)

print(mayor3, menor3)

# sol
numeros4 = []
mayor = None
menor = None

for num in numeros4:
    if mayor is None or num > mayor:
        mayor = num
    if menor is None or num < menor:
        menor = num

print(mayor)
print(menor)


# Reto 6
# Programa que muestra el reverso de una cadena de caracteres

cadena = "Hoy hace un dia estupendo."
reversa = cadena[::-1]

print(reversa)

# Reto 7
# Programa que comprueba si una cadena de caracteres es un palindromo.

cadena = "Allí por la tropa portado, traído a ese paraje de maniobras, una tipa como capitán usar boina me dejara, pese a odiar toda tropa por tal ropilla."

minusculas = cadena.lower()
palabras = minusculas.split()

lista_plana = []

for p in palabras:
    q = p.strip(".").strip(",")
    lista_plana.append(q)

candena_plana = "".join(lista_plana)
candena_plana = candena_plana.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

palindromo = candena_plana[::-1]

if candena_plana == palindromo:
    print("Son palindromos.")
else:
    print("No son palindromos")


# Reto 8
# Hallar numero capicua

inicial = 10000
final = 12000
capicuas = []

for numero in range(inicial, final + 1):
    cadena = str(numero)
    reverso = cadena[::-1]

    if cadena == reverso:
        capicuas.append(numero)

print(capicuas)