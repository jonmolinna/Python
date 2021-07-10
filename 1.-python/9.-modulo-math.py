from math import pi, pow, sqrt
import random

# 1.- Programa que calcule el area de un circulo (area = pi * radio al cuadrado)

radio = float(input("Ingrese el radio de un circulo:  "))
resultado = pi * (radio * radio)
print(f"El area del ciruclo es: {resultado}")

# 2.-Calcule la hipotenusa de un triangulo rectangulo sabien sus dos lados.

lado1 = float(input("Ingrese el lado 1:  "))
lado2 = float(input("Ingrese el lado 2:  "))
resultado = pow(lado1, 2) + pow(lado2, 2)
resultado = sqrt(resultado)
print(f"La Hipotenusa del triangulo es: {resultado}")

# 3.-Juego que genera un numero aleatorio del 1 al 100 y te pide que lo adivines.
# Se te va indicando si el numero que introduces es mayor o menor el que hay que adivinar.
# Tienes 7 intentos, si no el programa termina y te dice que has perdido.

numero = random.randint(1, 100)
conteo = 7
salir = False
adivina = False
while salir == False:
    number = int(input(f"adivine el numero de 1 al 100, tienes {conteo} intentos: "))
    if(conteo > 1):
        if(number > numero):
            print("El numero ingresado es mayor")
        elif(number < numero):
            print("El numero ingresado es menor")
        else:
            print("Adivinaste el Numero")
            adivina = True
            salir = True
    else:
        salir = True
    conteo -= 1

if adivina:
    print(f"felicitaciones adivinaste el numero con {7 - conteo} intentos")
else:
    print(f"No adivinaste el numero {numero}")


# 4.-Programa que simula 100 tiradas de una moneda y comprueba cuantas veces sale cada resultado posible.

caras = 0
cruces = 0
for i in range(100):
    lanzada = random.choice(["Cara", "Cruz"])
    if lanzada == "Cara":
        caras += 1
    elif lanzada == "Cruz":
        cruces += 1

print({"caras": caras, "cruces": cruces})