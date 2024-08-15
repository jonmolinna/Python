
# Metodo que abre y cierra el archivo
with open('test.txt') as file:
    print(file.read())

# test para verificar si el archivo esta cerrado
print(file.closed)

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('El archivo no fue encontrado')