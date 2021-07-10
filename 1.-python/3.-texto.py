ret = "* " * 5 + "+" + " *" * 5
ret2 = "a" + "b" + "c" < "acb"
print(ret2)

nombre = "Jorge"
apellido = "Garcia"
print(f"Me llamo {nombre} {apellido}")

# Tipos de Datos
# Entero(integer) -> int
# Flotante(floating) -> float
# Cadena(string) -> str

# Reto 2 + 2 = 4
print("2 + 2 = " + str(2 + 2))
print("2 + 2 =", 2 + int("2"))

nombre2 = input("¿Como te llamas?: ")
ciudad = input("¿De donde eres?: ")
print(f"Hola, {nombre2}, de {ciudad}. Encantado de conocerte.")


# ¿En que año estamos? fecha
# ¿Cuantos años tienes o vas a cumplir este año? edad
# Has nacido en el año:
fecha = int(input("¿En que año estamos?" ))
edad = int(input("¿Cuantos años tienes?" ))
print(f"Haz nacidp en el año {fecha - edad}.")