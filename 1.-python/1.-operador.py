# Tenemos 2 cajones de manzanas y nos traen otros 3 cajones.
# Si cada cajon tiene 20 manzanas, ¿Cuantas manzanas tendremos?
cajones = 5
manzanas = 5 * 20
print(manzanas)

# Hay que repartir una caja de bombones de 24 bombones entre 2 grupos de 3 alumnos cada uno
# ¿A cuantos bombones toca cada alumno?
alumnos = 3 * 2
total = 24 / alumnos
print(total)

# 5 es menor o igual que 10
# 5 es mayor o igual que 5
print(5 <= 10)
print(5 >= 5)

# 4 mas 3 es mayor que 6 menos 1
# 3 por 5 es distinto que 5 por 3
print(4 + 3 > 6 - 1)
print(3 * 5 != 5 * 3)

# 5 es mayor que 7 y 3 es menor que 4
# 8 es mayor o igual que 6 y 9 es distinto de 7
print(5 > 7 and 3 < 4)
print(8 >= 6 and 9 != 7)

# 2 mas 2 son 5 o 4 es igual a 4
# 3 por 2 son 8 o 5 es distinto de 5
print(2 + 2 == 5 or 4 == 4)
print(3 * 2 == 8 or 5 != 5)

# No es que 2 mas 2 sea igual a 4 (Negacion)
print(not 2 + 2 == 4)

# No es que 6 sea mayor que 2
# No es que 2 mas 2 sean 5
print(not 6 > 2)
print(not 2 + 2 == 5)

# No es que 3 mas 3 sea mayor que 2 por 3
print(not 3 + 3 > 2 * 3)

# Jerarquia de operadores logicos 1-not, 2-and, 3-or

# No es que 2 mas 2 sea igual a 5 o que 8 sea mayor que 3
print(not 2 + 2 == 5 or 8 > 3)

print(not (2 + 2 == 5 or 8 > 3))

# 5 por 2 es mayor que 9 y no es que 3 sea mayor que 4
print(5 * 2 > 9 and not 3 > 4)

# expresion
print(1 * 1 == 2 and 2 + 2 == 3 or 3 * 1 != 4)