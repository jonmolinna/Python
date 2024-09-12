# Ejemplo 1

feliz = True
print(feliz)

print(alegre := True)

# Ejemplo 2
comidas = []
while True:
    comida = input("¿Que comida te gusta? ")

    if comida == 'salir':
        break

    comidas.append(comida)


comidas = []
while (comida := input('¿Que comida te gusta? ')) != 'salir':
    comidas.append(comida)