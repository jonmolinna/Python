# reto 1

nombres = ["Susana", "Ruben", "Clara", "Jorge"]
edades = [18, 19, 20, 21]
amigos = [["Susana", 18], ["Ruben", 19], ["Clara", 20], ["Jorge", 21]]

for amigo in amigos:
    print("{:10}: {:2}".format(amigo[0], amigo[1]))


# Reto 2
# En una tienda quieren hacer un inventario de las figuras que tienen y el numero de unidades de cada una
# Crea una lista que contenga los datos del inventario: 6 cuadrados, 5 circulos, 4 triangulos y 3 rectangulos

figuras = [["Cuadrados", 6, [3,1]],
           ["Circulos", 5, [1,2]],
           ["Triangulos", 4, [2,2]],
           ["Rectangulos", 3, [4,3]]]

for f in figuras:
    print("{:12}: {:2}. Columna: {}. Fila {}".format(f[0], f[1], f[2][0], f[2][1]))

# Reto 3
# Pasar una lista bidimensional a dos listas unidimensionales, y viceversa: dos listas unidemensionales a una bidimensional

grupos = [[1, "A"], [2, "B"], [3, "C"], [4, "D"], [5, "E"], [6, "F"], [7, "G"], [8, "H"], [9, "I"], [0, "J"]]

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

numeros = []
letras = []

# Seperando los datos
for lista in grupos:
    numeros.append(lista[0])
    letras.append(lista[1])

# Uniendo los datos
grupo = []

for i in range(len(number)):
    grupo.append([number[i], chars[i]])


# Reto 4 Copia de Lista

import copy
p = [1, [2, 3], [4, 5, 6]]
q = copy.deepcopy(p)
print(p)
print(q)

p[0] = 10
p[1][0] = 20
p[2][0] = 40

print()
print(p)
print(q)

# Reto 5
# Aplanar una Lista

datos = [[1, 2, 3], 4, 5, [6, 7], 8, 9]
plana = []

for dato in datos:
    if type(dato) == int:
        plana.append(dato)
    elif type(dato) == list:
        for element in dato:
            plana.append(element)

# Otra forma
for dato in datos:
    if isinstance(dato, int):
        plana.append(dato)
    elif isinstance(dato, list):
        for element in dato:
            plana.append(element)

print(plana)