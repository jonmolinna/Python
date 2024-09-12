# Example 1
store = [
    ("camisa", 20),
    ("pantalones", 25),
    ("chaqueta", 50),
    ("medias", 10),
]

fun_dolar = lambda datos: (datos[0], datos[1] * 0.26)

store2 = list(map(fun_dolar, store))

for i in store2:
    print(i)