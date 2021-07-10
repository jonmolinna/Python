# Reto 1
# Define una funcion que tome como parametro un numero y devuelve el triple del doble de ese numero

# def funcion1(numero):
#     return 3 * (2 * numero)

# print(funcion1(10))


# Reto 2
# Definir una funcion que concatene dos cadenas de caracteres, las veces que se indique

# def concatena(cadena1, cadena2, veces):
#     return (cadena1 + cadena2) * veces

# c1 = input("Introduce una cadena: ")
# c2 = input("Introduce otra cadena: ")
# n = int(input("Introduce las veces: "))

# print(concatena(c1, c2, n))


# Reto 3
# Haz un programa con una funcion que muestre un saludo, dando la bienvenida al usuario, utilizando su nombre,
# el cual se ha pedido antes de llamar a la funcion. La funcion no devuelve nada (es decir, devuelve None).
# Definir la funcion con un parametro (el nombre del usuario)

# nombre = input("Ingrese su nombre: ")

# def funcion3(nombre):
#     print(f"Hola {nombre}. Bienvenido al Pais.")

# funcion3(nombre)


# Reto 4
# Hacer un programa que calcule la nota (en base a 10 puntos) de un examen que puede tener
# distinta cantidad de preguntas, y por cada fallo se reste una cierta cantidad de puntos.

# questionBad = float(input("Ingrese puntos que se reste por una nota mala: "))
# cantidadQuestion = int(input("Ingrese la cantidad de preguntas: "))
# cantidadAcierto = int(input("Ingrese la cantidad de aciertos: "))

# def funcion4(acierto):
#     resultado = ((10/cantidadQuestion) * acierto) - ((cantidadQuestion - acierto) * questionBad)
#     print(resultado)

# funcion4(cantidadAcierto)


# Reto 5
# Haz un programa en el que se compruebe si un numero es multiplo de otro, mediante una funcion con dos return

# number1 = int(input("Ingrese primer numero: "))
# number2 = int(input("Ingrese segundo numero: "))

# def es_multiplo_de(a, b):
#     if(a%b == 0):
#         return True
#     return False

# if es_multiplo_de(number1, number2):
#     print(f"{number1} y {number2} son divisibles")
# else:
#     print("No son divisibles")


# Reto 6
# Programa que convierte temperaturas:
# Fahrenheit a Celsius y Celsius a Fahrenheit.
# F = (C * 1.8) + 32 /// C = (F - 32) / 1.8

def cels_a_fahr(c):
    f = (c * 1.8) + 32
    return f

def fahr_a_cels(f):
    c = (f - 32) / 1.8
    return c

def menu():
    print("-----------------------")
    print("CONVERSOR TEMPERATURAS: ")
    print("1. Fahrenheit a Celsius")
    print("2. Celsius a Fahrenheit")
    print("3. Salir")
    opcion = input("-> ")
    return opcion

def pedir_grados(escala):
    if escala == "1":
        grados = float(input("Introduce °F: "))
    elif escala == "2":
        grados = float(input("Introduce °C: "))
    return grados

def mostrar_resultado(escala, grados):
    if escala == "1":
        print("Son", grados, "Celsius")
    elif escala == "2":
        print("Son", grados, "Fahrenheit")

# while True:
#     op = menu()
#     if op == "3":
#         break
#     elif op == "1" or op == "2":
#         gr = pedir_grados(op)
#         if op == "1":
#             conversion = fahr_a_cels(gr)
#         if op == "2":
#             conversion = cels_a_fahr(gr)
#         mostrar_resultado(op, conversion)
#     else:
#         print("Introduce una opcion correcta ")


# Reto 7
# Define una funcion que tome tres numeros y devuelva el que sea el intermedio de los tres.
# Si hay dos repetidos, se devuelve el repetido. Si hay tres repetidos, el unico que hay.

def numero_intermedio(a, b, c):
    ''' Funcion que toma tres numeros y devuelve el numero
        que sea el intermedio. Si hay dos repetidos, devuelve
        el repetido. Si hay tres repetidos, el numero que hay. '''

    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    elif a <= c <= b or b <= c <= a:
        return c

#help(numero_intermedio)
print(numero_intermedio(3, 1, 2))