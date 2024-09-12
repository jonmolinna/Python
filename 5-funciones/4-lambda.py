# lambda parametros : expression

# Ejemplo 1
def doble(x):
    return x * 2

print(doble(5))

result = lambda x : x * 2
print(result(10))

# Ejemplo 2
multiplicar = lambda x, y : x * y

print(multiplicar(4, 12))

# Ejemplo 3
verify_age = lambda age: True if age >= 18 else False

print(verify_age(27))