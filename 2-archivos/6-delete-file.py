import os
import shutil

try:
    os.remove('moving.txt')
    # os.rmdir('folder') -> delete folder vacia
    # shutil.rmtree('path') -> remove la carpeta y sus archivos
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('No tienes permiso para eliminar la carpeta')
except OSError:
    print('La carpeta tiene un archivo')