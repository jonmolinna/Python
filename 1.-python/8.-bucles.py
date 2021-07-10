# 1.-Programa que va mostrando en pantalla en una cuentra atraz los numeros del 10 al 0
# Utiliza un bucle for

for i in range(10, -1, -1):
    print(i)

# 2.-Programa que te pide 5 numeros y los va sumando. Al final te muestra el resultado

conteo = 1
suma = 0
while conteo <= 5:
    numero = int(input(f"Ingrese el numero {conteo}:  "))
    suma = suma + numero
    print(f"La suma es {suma}")
    conteo += 1
print(f"La suma de numeros es: {suma}")

#-------------------------------------------------------------------------
suma = 0
for i in range(5):
    n = float(input("Dime un numero:  "))
    suma += n
print("La suma es:", suma)

# 3.-Programa que va pidiendo numeros y los va sumando hasta que alcanza 100 o mas. Entonces para y muestra el total

suma = 0
while suma < 100:
    numero = float(input("Ingrese un Numero: "))
    suma = suma + numero
    print(f"La suma es: {suma}")

# 4.-Programa que pide un numero al usuario. Si ese numero mas algun numero de la lista dada es igual a 100,
# el programa dice que cumple con la condicion.
# Usar for e in

lista = [28, 36, 43, 52, 61, 75, 84, 97]
num = int(input("Dime un numero: "))

# ------ Usando la operador in
if 100 - num in lista:
    print("El numero cumple la condicion")
else:
    print("El numero no cumple la condicion")

# ------ Usando la operador for in
encontrado = False
for elemento in lista:
    if num + elemento == 100:
        encontrado = True

if encontrado == True:
    print("El numero cumple la condicion")
else:
    print("El numero no cumple la condicion")

# 5.-Programa que comprueba cuantas veces esta un numero en una lista dada

lista = [28, 36, 43, 52, 61, 43, 75, 84, 43, 97]
numero = 43
conteo = 0

for num in lista:
    if num == numero:
        conteo += 1

print(f"El numero {numero} en la lista hay {conteo} veces")

# 6.-Tenemos una tupla con los meses del año. Queremos saber que meses tienen en su nombre la letra "b"

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
lista = []

for char in meses:
    if "b" in char:
        lista.append(char)

print(lista)

# 7.-Programa que comprueba si un elemento esta en una lista y nos dice en que posicion (indice) se encuentra
# Utiliza un tipo range para recorrer la lista por sus indices

lista = [2, 5, 90, 23, 45, 87, 54, 11, 38]
elemento  = 54

for i in range(len(lista)):
    if lista[i] == elemento:
        print(f"El numero {elemento} esta en la posicion {i + 1}")


# 8.-Programa que muestra la tabla de multiplicar de un numero que le demos. (1-10)

numero = int(input("Ingrese un Numero:  "))

for i in range(10):
    resultado = (i+1) * numero
    print(f"{numero} x {i+1} = {resultado}")


# 9.-Tenemos una lissta de temperaturas. Hay que comprobar que todas las temperaturas esten entre 18 y 25 incluidos.
# Si alguna no cumple la condicion se para el programa y lo indica, sino va mostrando que la temperatura 
# verificada es correcta.

temperaturas = [19, 22, 21, 24, 23, 27, 21, 20, 19, 18, 21, 20]
for i in temperaturas:
    if i in range(18, 26):
        print("Temperatura es correcta")
    else:
        print("Temperatura incorrecta")
        break


# 10.-Programa un juego que te pide que adivines una letra, y te pide letras constantemente hasta
# que le adivines, y entonces se para.
# se puede probar con todas, menos con la 'w', en cuyo caso muestre que esa letra no esta
# permitida y se para el programa.

letra = 'w'
juego = True
while juego  == True:
    char = input("Ingrese una Letra:  ")
    if char == letra:
        print("Adivinastes la letra:  ")
        juego = False
    else:
        print("No es la letra, sigue adivianando")


# 11.-Programa que muestra si los numeros de una lista son pisitivos o negativos, a excepcion del cero
# que se lo salta.

numeros = [1, 4, -3, 5, 0, 7, -2, 6]

for i in numeros:
    if i < 0:
        print("Numero Negativo")
    if i > 0:
        print("Numero Positivo")
    if i == 0:
        continue