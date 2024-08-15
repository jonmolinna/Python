import os

origen = 'copy.txt'
destino = 'moving.txt'

try:
    if os.path.exists(destino):
        print('Ya existe el archivo')
    else:
        os.replace(origen, destino)
        print('El archivo fue movido')
except FileNotFoundError:
    print('File not found')