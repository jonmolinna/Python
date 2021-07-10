# Reto 1
def mayor_de_dos(a, b):
    ''' Funcion que toma dos numeros y devuelve el mayor '''
    if a > b:
        return a
    else:
        return b

def mayor_de_tres(a, b, c):
    ''' Funcion que toma tres numeros y devuelve el mayor '''
    # m = mayor_de_dos(a,b)
    # n = mayor_de_dos(m,c)
    # return n

    return mayor_de_dos(a, mayor_de_dos(b,c))

print(mayor_de_tres(1,2,3))
print(mayor_de_tres(1,3,2))
print(mayor_de_tres(2,1,3))


# Reto 2
# Define una funcion que tome tres numeros y devuelva el que sea el intermedio de los tres.
# Si hay dos repetidos, se devuelve el repetido. Si hay tres repetidos, el unico que hay.

def mayor_de_dos(a,b):
    if a > b:
        return a
    else:
        return b

def menor_de_dos(a,b):
    if a < b:
        return a
    else:
        return b

def intermedio_de_tres(a,b,c):
    if a < b:
        m = menor_de_dos(b,c)
        n = mayor_de_dos(m,a)
        return n
    else:
        m = menor_de_dos(a,c)
        n = mayor_de_dos(m,b)
        return n


# Reto 3
# Programa que simule una calculadora, utilizando funciones, que tenga las opciones:
# sumar, restar, multiplicar y dividir

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

def menu_calculadora():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = input("--> ")
    return opcion

n1 = float(input("Introduce numero: "))

while True:
    op = menu_calculadora()
    n2 = float(input("Introduce numero: "))

    if op == "1":
        resultado = sumar(n1, n2)
    elif op == "2":
        resultado = restar(n1, n2)
    elif op == "3":
        resultado = multiplicar(n1, n2)
    elif op == "4":
        resultado = dividir(n1, n2)

    print("Resultado: ", resultado)
    n1 = resultado

    seguir = input("Seguir operando (s/n): ")
    if seguir == "n":
        break


# Reto 4
# Programa con una funcion que convierte segundos en horas, minutos, y segundos
# Pide los segundos, y muestra el resultado.

def convertir_segundos(segundos):
    horas = segundos // 60 // 60
    minutos = segundos // 60 % 60
    segundos = segundos % 60
    return horas, minutos, segundos

cantidad_segundos = int(input("Introduce segundos: "))
h, m, s = convertir_segundos(cantidad_segundos)
print("Tiempo: {}:{}:{}".format(h, m, s))