import time
import random

# 1.-Programa donde jugamos a que pase el tiempo

inicio = time.time()
while True:
    print("Estamos Jugando ...")
    final = time.time()
    if final - inicio >= 5:
        break

print("Fin del Juego.")
print("Tiempo de Juego", final - inicio)

# 2.-Programa que lleva a cabo una cuenta atras de 10 segundos:
#   1. Muestra cada segundo (10-9-8-7-6....)
#   2. Muestra cada 5 decimas de segundo (10-9.5-9-8-8.5)
# Mide el tiempo para comprobar que transcurren 10 segundos

inicio = time.time()

for i in range(11):
    print(10-i)
    time.sleep(1)

final = time.time()

print("Tiempo: ", final - inicio - 1)

# 3.-Calcula la suma de los numeros del 1 al un millon:
#   1 + 2 + 3 + 4 + 5 ...... + 1_000_000
# Hazlo con 'while' y 'for' y mide el tiempo de ejecucion.

inicio = time.perf_counter()
suma = 0
n = 1

while n < 1_000_001:
    suma += n
    n += 1

final = time.perf_counter()
print("La suma es: ", suma)
print("Tiempo con while es: ", final - inicio)


# 4.-Juego de memoria. Te muestra cuatro coleres y te da tres segundos para recordarlos en el orden en que aparecian
# Si aciertas te los que vuelve a mostrar en otro orden distinto

colores = ["azul", "rojo", "verde", "blanco"]
print()
print("Memoriza los Colores")
print()
puntos = 0

while True:
    random.shuffle(colores)

    print("... Preparado ...")
    time.sleep(1)
    print("... Listo ...")
    time.sleep(1)
    print("...... Ya ......")

    # Muestra los colores
    for i in range(len(colores)):
        print(" ", colores[i], end=" ")
    print()
    time.sleep(3)

    for i in range(10):
        print("*" * i * 5)
    for i in range(10,0,-1):
        print("*" * i * 5)

    print()
    print("Dime los colores: ")
    color1 = input("Primero:  ")
    if color1 == colores[0]:
        color2 = input("Segundo: ")
        if color2 == colores[1]:
            color3 = input("Tercero: ")
            if color3 == colores[2]:
                color4 = input("Cuarto:  ")
                if color4 == colores[3]:
                    puntos += 1
                    print("Has acertado. Tienes", puntos, "punto.")
                    print()
                else:
                    print("No has acertado. Has perdido")
                    break
            else:
                print("No has acertado. Has perdido")
                break
        else:
            print("No has acertado. Has perdido")
            break
    else:
        print("No has acertado. Has perdido")
        break

print("Has conseguido", puntos, "Puntos")


# 5.-Juego de memoria. Te muestra cuatro colores de una lista de 10 y te da tres segundos para recordarlos
# en el orden en que aparecian. Si aciertas te los vuelve a mostrar en otro orden distinto.

colores = ["azul", "rojo", "verde", "blanco", "negro", "amarrillo", "naranja", "rosa", "morado", "marron"]
print()
print("Memoriza los Colores")
print()
puntos = 0

while True:
    muestra = random.sample(colores, 4)

    print("... Preparado ...")
    time.sleep(1)
    print("... Listo ...")
    time.sleep(1)
    print("...... Ya ......")

    # Muestra los colores
    for i in range(len(muestra)):
        print(" ", muestra[i], end=" ")
    print()
    time.sleep(3)

    for i in range(10):
        print("*" * i * 5)
    for i in range(10,0,-1):
        print("*" * i * 5)

    print()
    print("Dime los colores: ")
    color1 = input("Primero:  ")
    if color1 == muestra[0]:
        color2 = input("Segundo: ")
        if color2 == muestra[1]:
            color3 = input("Tercero: ")
            if color3 == muestra[2]:
                color4 = input("Cuarto:  ")
                if color4 == muestra[3]:
                    puntos += 1
                    print("Has acertado. Tienes", puntos, "punto.")
                    print()
                else:
                    print("No has acertado. Has perdido")
                    break
            else:
                print("No has acertado. Has perdido")
                break
        else:
            print("No has acertado. Has perdido")
            break
    else:
        print("No has acertado. Has perdido")
        break

print("Has conseguido", puntos, "Puntos")