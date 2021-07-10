# Mas Operadores Aritmeticos
# /     -       division
# //    -       division sin resto (division entera)
# %     -       resto de la division (modulo)

# 1.- Programa que dado un numero de caramelos y un numero de niños, diga a cuantos caramelos
# toca a cada niño y cuantos caramelos sobran

nino = int(input("Ingrese Cantidad de niños:  "))
caramelo = int(input("Ingrese Cantidad de caramelos:  "))
toca = caramelo // nino
sobran = caramelo % nino
print(f"Repartir {caramelo} caramelos entre {nino} niños")
print(f"A cada niño le toca {toca} caramelos.")
print(f"Sobran {sobran} caramelos")


# 2.-Programa que transforma un tiempo dado en segundos en sus horas, minutos, y segundos correspondientes.
# Introducir el dato: 174452 segundos y nos tiene que dar 48 horas 27 minutos y 32 segundos

segundos = int(input("Ingrese un tiempo en segundos:  "))
minutos = segundos // 60            # Pasame los segundos a minutos
segundos_resto = segundos % 60      # Segundos que sobran
horas = minutos // 60               # Pasamos los minutos a horas
minutos_resto = minutos % 60        # Minutos que sobran
print(f"Tiempo: {segundos}, {horas} H, {minutos_resto} M, {segundos_resto} S")


# 3.-Programa que comprueba si un numero dado es par o impar

numero = int(input("Ingrese un Numero:  "))
if(numero % 2 == 0):
    print(F"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")


# 4.-Programa que comprueba si un numero es multiplo de 3, de 5, o de los dos

numero = int(input("Ingrese un Numero:  "))
if numero % 15 == 0:
    print(f"El numero {numero} es multiplo de 3 y 5")
elif numero % 5 == 0:
    print(f"El numero {numero} es multiplo de 5")
elif numero % 3 == 0:
    print(f"El numero {numero} es multiplo de 3")
else:
    print(f"El numero {numero} no es multiplo de 3 ni 5")


# 5.-Programa que dados tres numeros, encuentra cual es el mayor de los tres

num1 = int(input("Ingrese primer numero:  "))
num2 = int(input("Ingrese segundo numero:  "))
num3 = int(input("Ingrese tercer numero:  "))
if num1 > num2 and num1 > num3:
    print(f"El numero {num1} es mayor de {num2} y {num3}")
elif num2 > num1 and num2 > num3:
    print(f"El numero {num2} es mayor de {num1} y {num3}")
else:
    print(f"El numero {num3} es mayor de {num1} y {num2}")


# 6.-Programa que te pide que te inventes una constraseña y que luego la repitas dos veces mas.
# Despues comprueba que lo has hecho conrrectamente.

contra = input("Cree una Contraseña:  ")
contador = 1
while contador < 3:
    primer = input("Ingrese nuevamente la contraseña:  ")
    if(contra == primer):
        print("La contraseña es conrrecto")
        contador = contador + 1
    else:
        print("La constraseña es incorrecto")


# 7.-Programa que pide un numero del 0 al 10 y comprueba si introduces un numero correcto

contador = False

while contador == False:
    numero = int(input("Ingrese numero de 0 al 10:  "))
    if(numero >= 0 and numero <= 10):
        print("Numero ingresado es correcto")
        contador = True
    else:
        print("Numero ingresado es falso, intente de nuevo")