# 1.-Crea una variable "d" a partir de las variables a, b y c que contenga la cadena de caracteres "partitura"

a = "altura"
b = "parte"
c = "cristal"
d = b[:4] + c[2:3] + a[2:]
print(d)

# 2.-Mostrar en pantalla las letras que forman la palabra "mariposa"

letra = "mariposa"
for char in letra:
    print(char)

# 3.-Comprobar cuantas veces aparece el caracter "o", con o sin tilde, en la siguiente cadena de caracteres

cadena = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo."
cadena = cadena.lower()
contar = 0
for char in cadena:
    if char == "o" or char == "ó":
        contar += 1
print(contar)

# 4.-Programa que te dice las vocales que tiene una palabra

palabra = input("Dime una palabra:  ")
vocales = "aeiouáéíóú"
indice = 0
num_voc = 0

while indice <= len(palabra) - 1:
    if palabra[indice] in vocales:
        num_voc += 1
    indice += 1
print("El numero de vocales es: ", num_voc)

# 5.-Programa que te dice las vocales y las consonantes que tiene una palabra que introduzca el usuario

palabra = input("Dime una palabra: ")
palabra = palabra.lower()
vocales = "aeiouáéíóú"
consonantes = "qwrtypsdfghjklñzxcvbnm"
indice = 0
num_vocales = 0
num_consonantes = 0
while indice <= len(palabra) - 1:
    if palabra[indice] in vocales:
        num_vocales += 1
    if palabra[indice] in consonantes:
        num_consonantes += 1
    indice += 1
print({"vocales" : num_vocales, "consonantes" : num_consonantes})

# 6.-Tenemos tres tuplas:
# Crea una tupla a partir de ellas que contenga las mascotas

mamiferos = ("tigre", "gato", "leon")
aves = ("aguila", "buitre", "canario")
reptiles = ("tortuga", "serpiente")
mascotas = mamiferos[1:2] + aves[2:] + reptiles[0:1]
print(mascotas)

# 7.-Litas
# Crea un Lista que contenga los numeros enteros del 1 al 100 utilizando un bucle while, y partiendo
# de una lista vacia

lista = []
numero = 1
while numero <= 100:
    lista.append(numero)
    numero += 1
print(lista)


# 8.-Programa que pida un numero entero que este en el intervalo del 18 al 25, y que siga pidiendo
# numeros mientras de mantengas en ese intervalo. Utiliza el tipo range

intervalo = range(18, 26)
numero = int(input("Ingrese un numero entre 18 y 25:  "))
while numero in intervalo:
    numero = int(input("Ingrese un numero entre 18 y 25:  "))

# 9.- Crea un juego "Ruleta de los coleres"

colores = ["blanco", "rojo", "azul", "morado", "negro"]
adivina = True
puntos = 0

while adivina == True:
    color = input("Ingrese un color de la ruleta:  ")
    if color in colores:
        print("Genial adivinastes un color")
        puntos += 1
        print(f"tienes {puntos} puntos")
    else:
        print("El color no existe en la ruleta")
        adivina = False

print(f"El juego termino tuvistes {puntos} puntos")