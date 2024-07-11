edad = 28

if edad >= 19:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Example 1
#  separe en un array los numeros pares y impares

def numbers(arr: list):
    par = []
    impar = []

    for x in arr:
        if x % 2 == 0:
            par.append(x)
        else:
            impar.append(x)

    print(par)
    print(impar)
            
# numbers([1, 2, 3, 4, 5, 6, 7, 8,9, 10])

# Example 2
# Traer el numero mayor y el menor de una lista
def menorMayor(array: list):
    menor = array[0]
    mayor = 0

    for x in array:
        if (x > mayor):
            mayor = x
        if (x < menor):
            menor = x


    return {"menor": menor, "mayor": mayor }

result = menorMayor([7,10, 5, 9, 23, 2, 12])
# print(result)

# Example 3
# Obtener de 1 al 20, cual de ellos es el numero primo
def primos(number: int):
    for x in range(2, number):
        if number % x == 0:
            return False
        
    return True
    

def numeros():
    array = []
    for x in range(2, 21):
        result = primos(x)

        if(result):
            array.append(x)

    return array

result = numeros()
# print(result)