# Programe que pide la edad al usuario y averigua si es mayor de edad

edad = int(input("Ingrese su edad: "))
if(edad > 17):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Programe que pida dos numeros que sumen 10 entre los dos
# Si aciertas, que muestre: "Has acertado"
# Si no aciertas que muestre: "No has acertado."

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
if(a + b == 10):
    print("Has acertado")
else:
    print("No has acertado")

# Programa que pide dos numeros y que dice cual es mayor de los dos

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
if(a > b):
    print(f"el numero {a} es mayor que {b}")
elif(a == b or b == a):
    print(f"el numero {a} es igual a {b}")
else:
    print(f"el numero {b} es mayor que {a}")

# Programa que pida tu edad y la edad de un amigo. y que diga cual es mayor de los dos
# se empieza comprobando la condicion de que las edades sean iguales

edad = int(input("Ingrese tu edad: "))
edad2 = int(input("Ingrese tu edad: "))
if(edad > edad2):
    print(f"la edad {edad} es mayor a {edad2}")
elif(edad == edad2):
    print(f"la edad {edad} es igual a {edad2}")
else:
    print(f"la edad {edad2} es mayor a {edad}")

# Programa que simula una maquina de refresco.
# la maquina dispone de 4 tipos de refresco.
# te pide el numero de refresco que deseas entre el 1 el 4
# te informa tu eleccion

numero = int(input("Eliga un refresco de 1 al 4: "))
if(numero == 1):
    print("Elegiste el regresco 1")
elif(numero == 2):
    print("Elegiste el regresco 2")
elif(numero == 3):
    print("Elegiste el regresco 3")
elif(numero == 4):
    print("Elegiste el regresco 4")
else:
    print("no existe esa categoria")


# Programa que pida la edad de una persona e informa de cuatro posibilidades:
# Si la edad es mayor o igual que 25: "Es un adulto."
# si la edad es mayor o igual que 70: "es un anciano"
# si la edad es mayor o igual que 14: "es un joven"
# sino si es menor de 14 es un niño

edad = int(input("Ingrese un edad:  "))
if(edad > 0 and edad < 14):
    print("Es un niño")
elif(edad >= 14 and edad <= 24):
    print("Es un Joven")
elif(edad >= 25 and edad < 70):
    print("Es un adulto")
elif(edad >= 70 and edad <=100):
    print("Es un anciano")
else:
    print("No hay edad")


# Siguiente reto
print(8 == 4+4 and 8 == 4*2 and not 8 == 4*4)


# Programa que simula la entrada a una atraccion en un parque de atracciones, y pide la edad y el peso en kilos.
# Por seguridad, para poder subir tienes que tener mas de 12 años y pesar mas de 45 kilos,
# sino no puedes subir

edad = float(input("Ingrese su Edad:  "))

if edad > 12:
    peso = float(input("Ingrese su Peso:  "))
    if peso > 45:
        print("Puedes subir al juego mecanico")
    else:
        print("Lo sentimos usted no puede subir al juego")
else:
    print("No cuentas con suficiente edad")