class Auto:

    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def encendido(self):
        print('El auto esta encendido!')

    def apagado(self):
        print('El auto esta apagado')