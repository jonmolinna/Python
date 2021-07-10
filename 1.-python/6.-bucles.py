# Operadores Compuestos de Asignacion
# n = n + 1     =>      n += 1
# n = n - 2     =>      n -= 2
# n = n * 3     =>      n *= 3
# n = n / 4     =>      n /= 4

# 1.-Programa que muestre en pantalla un secuencia de numeros del 20 al 0

contador = 20
while contador >= 0:
    print(contador)
    contador = contador - 1


# 2.-Programa que te pide que introduzcas un numero que este entre el 10 y el 20. Si es correcto te diga que estas
# en el rango, y te pida otro. Hasta que le des un numero fuera de rango y se acabe el programa.

contador = False
while contador == False:
    numero = int(input("Ingrese un Numero de 10 al 20:  "))
    if numero >= 10 and numero <= 20:
        contador = False
    else:
        contador = True


# 3.-Programa que te pide que adivines un numero del 1 al 10 y te pida numeros constantemente hasta que lo
# adivinez. Añade un contador que te diga los intentos que has necesitado
# Conviene que crees tres variables, y utiliza un "else"

import random

aleatorio = random.randint(1, 10)
contador = 0
adivina = False
while adivina == False:
    numero = int(input("Adivine el Numero del 1 al 10:  "))
    if numero == aleatorio:
        print("Felicitaciones adivinaste el numero")
        adivina = True
    contador = contador + 1

print(f"Numero de Intentos {contador}")


# 4.-Programe que sume los numeros del 1 al 10

n = 1
suma = 0
while n <= 10:
    suma += n
    n += 1
print(suma)


# 5.-Programa que suma los numeros pares que hay entre el 1 y el 20

numero = 1
suma = 0
while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print(suma)


# 6.-Programa que pide un numero de inicio y el otro final al usuario,
# y que sume todos los numeros multiplos de 3 que hay entre ellos

numero1 = int(input("Ingrese un numero de inicio:  "))
numero2 = int(input("Ingrese un numero final:  "))
suma = 0
while numero1 <= numero2:
    if numero1 % 3 == 0:
        suma += numero1
    numero1 += 1
print(suma)


# 7.-Programa que pide el usuario y el contraseña.
# Si no pones los dos correctamente te los vuelve a pedir
# PLANTANDO UNA BANDERA

usuario = "brehn"
contrasena = "1234"
correcto = False
while correcto == False:
    user = input("Ingrese su Usuario:  ")
    password = input("Ingrese su Contraseña:  ")

    if user == usuario and contrasena == password:
        correcto = True
        print("Felicitaciones Ingresastes al Sistema")
    else:
        print("Contraseña o Usuario Incorrecto intente nuevamente")


# Juego que pregunta un numero del 1 al 5 y luego una vocal.
# Tienes 100 puntos, si aciertas uno de ellos te quita 2 puntos, si no aciertas ninguno te quita 5 puntos.
# El programa no se acaba hasta que aciertes los dos.
# Cuando se acaba el programa te dice los puntos que te quedan

numero = "3"
vocal = "u"
puntos = 100
jugando = True

while jugando:
    intento_numero = input("Dime un numero del 1 al 5:  ")
    intento_vocal = input("Dime una letra vocal:  ")
    if intento_numero != numero and intento_vocal != vocal:
        puntos -= 5
        print("No has acertado ninguno. Te quedan", puntos, "Puntos")
    elif intento_numero != numero or intento_vocal != vocal:
        puntos -= 2
        print("No has acertado uno. Te quedan", puntos, "Puntos")
    else:
        print("Has acertado. Tus puntos restantes son", puntos)
        jugando = False

print("Fin del Juego")