import math

# Reto 1
# Tomar el valor absoluto de un numero

x = -20
print(abs(x))

def valor_absoluto(numero):
    if numero >= 0:
        return numero
    else:
        return - numero
print(valor_absoluto(x))

# Reto 3
# Define una funcion que calcule la potencia de un numero

x = 10
print(x**3)
print(pow(10,3))

def potencia(base, exponente):
    numero = 1
    i = 1
    while i <= exponente:
        numero *= base
        i += 1
    print(numero)

potencia(10,3)

# Reto 4
# Define una funcion que calcule la raiz cuadrada de un numero

x = 1234
print(math.sqrt(x))

def raiz_babilonica(n):
    x = n / 2
    while True:
        if x * x == n:
            return x
        else:
            copia_x = x
            x = (x + (n/x))/2
        if copia_x == x :
            break
    return x

print(raiz_babilonica(x))


# Reto 5
# funcion factorial

x = 5
print(math.factorial(x))

def my_factorial(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f
print(my_factorial(x))


# Reto 6
# Calcule el numero de combinaciones sin repeticion de m elementos tomados de n en n.
# reuire de una funcion factorial

def numero_combinaciones(m,n):
    if m < n:
        return 0
    else:
        comb = math.factorial(m) / (math.factorial(n) * math.factorial(m-n))
        return comb

print(numero_combinaciones(10, 5))

# En forma eficiente
def numero_combinaciones_simplificada(m,n):
    dif = m - n
    f = 1
    while m > dif:
        f = f * m
        m -= 1
    g = 1

    while n > 0:
        g = g * n
        n -= 1
    return f / g

print(numero_combinaciones_simplificada(10, 5))


# Reto 7
# Adivinar numero primos

def es_primo(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(es_primo(17))


# Reto 8
# Numero primo optimizado

def es_primo_2(num):
    if num < 2:
        return False
    raiz = int(math.sqrt(num)) + 1

    for i in range(2, raiz):
        if num % i == 0:
            return False
    return True

print(es_primo_2(17))


# Reto 9
# Haz un programa con una funcion que ecuentre todos los numeros primos que hay en un intervalo
# de numeros que indique el usuario

a = int(input("Numero Inicial: "))
b = int(input("Numero Final: "))

def econtrar_primos(inicial, final):
    primos = []

    for n in range(inicial, final + 1):
        contador = 0
        for i in range(1, n+1):
            if n % i == 0:
                contador += 1
        if contador == 2:
            primos.append(n)
    return primos

print(econtrar_primos(a, b))

#----------------------------------------------------------------

def encontrar_primos_2(inicial, final):
    primos = []

    if inicial < 2:
        inicial = 2

    for n in range(inicial, final + 1):
        es_primo = True
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
    return primos

print(encontrar_primos_2(a, b))

def encontrar_primos_3(inicial, final):
    primos = []

    if inicial < 2:
        inicial = 2

    for n in range(inicial, final + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            primos.append(n)
    return primos

print(encontrar_primos_3(a, b))


# Reto 10
# Funcion que descompone un numero en los factores primos de los que esta compuesto

def descomponer(n):
    primos = []

    for i in range(2, n+1):
        while n % i == 0:
            primos.append(i)
            n = n / i
    return primos

print(descomponer(60))


# Reto 11
# Funcion que halla los multiplos de un numero (algunos)
# Funcion que halla los divisores de un numero (todos)
# (Estamos en el ambito de los numeros enteros positivos)

def multiplos_hasta_limite(numero, limite):
    multiplos = []
    i = 1
    multiplo = numero

    while multiplo <= limite:
        multiplos.append(multiplo)
        i += 1
        multiplo = numero * i
    return multiplos

print(multiplos_hasta_limite(12, 100))

#--------------------------------------------------------------

def multiplos_hasta_cantidad(numero, cantidad):
    multiplos = []
    i = 1
    while len(multiplos) < cantidad:
        multiplo = numero * i
        multiplos.append(multiplo)
        i += 1
    return multiplos

print(multiplos_hasta_cantidad(12, 8))

def hallar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

print(hallar_divisores(30))


# Reto 12
# Funcion que devuelve el Maximo comun divisor de dos numeros

def halla_divisores(n):
    divisores = []
    for i in range(1, n+1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def mod_divisores_comunes(n1, n2):
    d1 = halla_divisores(n1)
    d2 = halla_divisores(n2)

    divisores_comunes = []

    for i in d1:
        if i in d2:
            divisores_comunes.append(i)

    mayor = max(divisores_comunes)
    return mayor

print(mod_divisores_comunes(60, 48))


def mod_fuerza_bruta(n1, n2):
    if n1 < n2:
        i = n1
    else:
        i = n2

    while not (n1 % i == 0 and n2 % i == 0):
        i -= 1
    else:
        return i

print(mod_fuerza_bruta(11990, 5032))

def mcd_euclides(n1, n2):
    while True:
        resto = n1 % n2
        if resto == 0:
            return n2
        else:
            n1 = n2
            n2 = resto

print(mcd_euclides(60, 48))


# Conjetura de Collatz
# Para todo numero entero positivo:
#   - Si es par se divide entre 2
#   - Si es impar se multiplica por 3 y se suma 1.
# Llevando a cado estas operaciones sucesivamente sobre el numero resultante,
# como resultado final siempre se alcanza el numero 1

# -> 6 : 6-3-10-5-16-8-4-2-1
# -> 11 : 11-34-17-52-26-13-40-20-10-5-16-8-4-2-1

# 1.- Definir una funcion que compruebe que la conjetura
# de collatz se cumple para un numero dado.

# 2.- Comprobar que la conjetura de collatz se cumple para todos los numeros enteros del 1 al 1 millon

def collatz(num):
    sec = [num]

    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

        sec.append(num)
    return sec

#print(collatz(6))


# Conjetura de Goldbach
# Todo numero par mayor que 2 se puede expresar como la suma de dos numeros primos
# Para el numero 14 tendriamos: 3 y 11, 7 y 7
# (1 y 13 no valdrian, ya que el 1 no es considerado primo)
# Hacer un programa que muestre todas las parejas de primos en las que se puede expresar un numero par mayor que 2

def es_primo_4(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num4 = int(input("Numero par mayor que 2: "))

for a in range(2, num4):
    if es_primo_4(a):
        b = num4 - a
        if es_primo_4(b):
            if a <= b:
                print("Primos", a, b)