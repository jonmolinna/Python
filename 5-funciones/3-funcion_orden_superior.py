# Ejemplo 1
def hablarAlto(texto: str):
    return texto.upper()

def hablarBajo(texto: str):
    return texto.lower()

def holaMundo(func):
    texto = func('Hola a todos')
    print(texto)

holaMundo(hablarAlto)
holaMundo(hablarBajo)

# Ejemplo 2
def divisor(x):
    def dividiendo(y):
        return y / x
    
    return dividiendo

divide = divisor(2)
print(divide(10))