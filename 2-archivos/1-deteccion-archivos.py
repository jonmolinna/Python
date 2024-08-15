import os

path = "C:\\Users\\LENOVO\\Desktop\\Python\\2-archivos\\test.txt"

if os.path.exists(path):
    print('Si existe el archivo')

    if os.path.isfile(path):
        print('Es un archivo')
    elif os.path.isdir(path):
        print('Es un directorio')
else:
    print('No existe el archivo')