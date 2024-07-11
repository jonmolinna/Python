# Manipular Cadenas
name = "kendra contreras"

cadena = name[0: 3]

# Example 1
# Extraer las primareras palabras de una cadena
def charAt(str: str) :
    array = str.split(" ")
    result = map(lambda x : x[0:1].upper()  , array)
    res = "".join(result)
    return res


result = charAt("emma saez")
print(result)