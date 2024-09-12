# Example 1
cuadrado = []

for i in range(1, 11):
    cuadrado.append(i * i)

print(cuadrado)

new_cuadrado = [i*i for i in range(1, 11)]

print(new_cuadrado)

# Example 2
notas = [20, 19, 18, 17, 16, 15]

apro = list(filter(lambda x : x >= 17, notas))
print(apro)

new_apro = [i for i in notas if i >= 17]
print(new_apro)
