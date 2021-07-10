# Programa 1

nombre = input("Hola, ¿Quien eres?  ")
# nombre = nombre.title()
# nombre = nombre.capitalize()
nombre = nombre.lower()
name = nombre[0].upper() + nombre[1:]
print(f"Hola {name}")
res = input(f"Estas seguro que eres {name.upper()}:  ")

if res.lower() == 's':
    print("Vale")
else:
    print("No te entiendo")


# 2.-Programa que recoge todas las palabras de un texto y las devuelve sin espacios, comas ni puntos

cadena = "Estaba alli. Era un pájaro, en la ventana. Pero entonces, de repente, se echo a volar."
arr = cadena.split()
lista = []

for char in arr:
    if char[-1] == ".":
        lista.append(char.strip('.'))
    elif char[-1] == ",":
        lista.append(char.strip(','))
    else:
        lista.append(char)

for char in lista:
    print(char)

# # Otra forma de hacer
palabras = cadena.split()
for p in palabras:
    m = p.strip(",")
    n = m.strip(".")
    print(n)


# 3.-Programa que pide datos (tratamiento, nombre y apellidos) de las personas que han sido invitadas a una fiesta,
# para enviarlas una carta de invitacion. Luego se muestra en pantalla la carta con los datos que se piden,
# y se pregunta si se quiere introducir nuevos datos de otra persona. 

imprime = True
while imprime == True:
    print("MODELO DE CARTA")
    print("Introduzca los datos de la persona: ")
    tratamiento = input("Tratamiento (Sr/Sra):  ")
    nombre = input("Nombre:  ")
    apellido = input("Apellidos:  ")
    tratamiento = tratamiento.upper().title()
    nombre = nombre.upper().title()
    apellido = apellido.upper().title()

    print(f"{tratamiento}. {nombre} {apellido}")
    print("Le escribo para informarle")
    if tratamiento[-1] == 'a':
        inv = "intatada"
    else:
        inv = "invitado"
    print(f"de que ha sido usted {inv}")
    print("a la fiesta de la empresa.")
    print("Atentamente.")

    continua = input("Desea imprimir otra carta (s/n):  ")
    continua = continua.strip("")
    if continua.lower() == "s":
        imprime = True
    elif continua.lower() == "n":
        imprime = False
    else:
        print("No te entiendo.....")
        imprime = True


# 4.- Mas formateo

print()
print("PRESUPUESTO".center(50))
print()

compras = [["Tornillos", 723, 23.2],
           ["Tuercas", 324, 4.5],
           ["Arandelas", 25, 35],
           ["Puntas", 1431, 2.15]]

for c in compras:
    print("{0:12} : {1:8d} * {2:8.2f} = {3:12.2f}".format(c[0], c[1], c[2], c[1]*c[2]))


# 6.-Programa que crea una lista con 100 elementos, que son los numeros enteros del 1 al 100

lista = []
for num in range(1, 101):
    lista.append(num)

print(lista)


# 7.-Tenemos una lista de numeros y queremos separar los pares de los impares, y guardarlos en otras
# dos listas Hazlo con el metodo append

numeros = [2, 3, 5, 8, 9, 12, 21, 24, 25, 28]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(pares)
print(impares)


# 8.-Programa que te pida que introduzcas productos y crea una lista de la compra con esos productos que te
# muestra al final

lista = []

ingresa = True
while ingresa == True:
    producto = input("Ingrese un Producto:  ")
    lista.append(producto)

    continua = input("¿Desea ingresar mas prodcutos? (s/n):  ")

    if continua.lower() == "n":
        ingresa = False

print()
print("Lista de productos")
for char in lista:
    print(char)


# 9.-Crea una lista con los numeros enteros del 1 al 5, a partir de los datos que se te dan.
# Usa los metodos append o extend, segun mejor convenga.

n = [1, 2, 3]
m = [4, 5]

o = [1, 2, 3, 4,]
p = [5]

n.extend(m)
o.extend(p)

print(n)
print(o)


# 10.- Crea una lista con los numeros enteros del 1 al 5, a partir de los datos que se te dan.
# Usa los metodos append, extend o insert, segun mejor convenga

m = 1
n = [2, 3]
s = [4]
t = 5

n.extend(s)
n.insert(0, m)
n.append(t)

print(n)



# Metodos
# char.strip() => elimina los espacios
# char.split() => divide las palabras en arreglos