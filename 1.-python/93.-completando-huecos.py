# Reto 1

eleccion = None

while eleccion is None or eleccion > 5:
    eleccion = int(input("Dime un numero mayor que 5:  "))
else:
    print("Has elegido un numero menor que 5.")


# Reto 2
# Programa que pide 7 numeros y comprueba que numero es el mayor

lista = []
i = 1
numero = None
mayor = 0

while i <= 7:
    numero = int(input(f"Ingrese el numero {i}:  "))
    lista.append(numero)
    i += 1

for num in lista:
    if num > mayor:
        mayor = num
print(f"El numero mayor ingresado es: {mayor}")

# Otra forma de hacer

mayor = None

for i in range (7):
    n = int(input("Dime un numero:  "))
    if mayor is None or n > mayor:
        mayor = n
print("El numero mayor es:", mayor)


# Reto 3
# Programa que pide que tres jugadores introduzcan un numero y espera a que los tres jugadores
# hayan introducido el numero

print("ELIGIENDO UN NUMERO LOS JUGADORES")
jugador1 = None
jugador2 = None
jugador3 = None

while jugador1 is None or jugador2 is None or jugador3 is None:
    print()
    print("Pulsa:")
    print("1. Para jugador A")
    print("2. Para jugador B")
    print("3. Para jugador C")
    print()
    jugador = int(input("Elige jugador:  "))
    if jugador == 1 and jugador1 is None:
        jugador1 = int("Dime un Numero: ")
    elif jugador == 1 and jugador1 is not None:
        print("El jugador 1 ya ha elegido")
    elif jugador == 2 and jugador2 is None:
        jugador2 = int(input("Dime un Numero: "))
    elif jugador == 2 and jugador2 is not None:
        print("El jugador 2 ya ha elegido")
    elif jugador == 3 and jugador3 is None:
        jugador3 = int(input("Dime un Numero: "))
    elif jugador == 3 and jugador3 is not None:
        print("El jugador 3 ya ha elegido")
    else:
        print("Has introducido una opcion incorrecta")

else:
    print()
    print("Los tres jugadores ya han elegido numero:")
    print(" Jugador A:", jugador1)
    print(" Jugador B:", jugador2)
    print(" Jugador C:", jugador3)


# Reto 4
# Crea una lista vacia llamada "Letras" (usando una funcion)
# Añade la letra 'a' a esa lista (usando un metodo)
# Haz una copia de la lista (creado una lista distinta)
# Añade la letra "b" a la copia de la lista
# Comprueba los elementos de las dos lista

letras = list()
letras.append("a")
copia_letras = list(letras)
copia_letras.append("b")

print(letras)
print(copia_letras)

# Reto 5
# crea una lista nueva que sea el reverso de la lista dada

numeros = [1, 5, 8, 4, 7, 2, 9]
numero_iversa = list(reversed(numeros))
numeroInve = numeros[::-1]
print(numeros)
print(numero_iversa)
print(numeroInve)

# Reto 6
# Crea una lista "cuenta_adelante" que contenga los elementos de la lista "cuenta_atras" pero en orden iverso.
# utiliza el metodo reverso().

cuenta_atras = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
cuenta = cuenta_atras[::-1]

print(cuenta_atras)
print(cuenta)

# Reto 7
# Ordena la Lista

edades = [12, 18, 42, 21, 24, 13, 21, 35, 17, 23]
ordenEdad = sorted(edades)
print(ordenEdad)


# Datos
# None => se usa para iniciar un dato
# is => se usa para comparar una identidad = m = 2, n = 2 m is n => true id(m)
# reversed()
# sorted()
# sort()