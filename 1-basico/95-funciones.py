def saludo(name):
    print('Hola', name)

saludo('Cortana')

# Return
def sumar(a, b):
    return a + b

result = sumar(10, 20)
print(result)

# *args => tuplas
def sumar2(*args):
    suma = 0

    for i in args:
        suma += i

    return suma

result = sumar2(1, 2, 3, 4)
print(result)

# **kwargs => diccionario
def names(**kwargs):
    # print(kwargs['name'] + ' ' + kwargs['surname'])
    for key, value in kwargs.items():
        print(value, end=' ')

names(name='Kendra', surname='Contreras', age=28)


