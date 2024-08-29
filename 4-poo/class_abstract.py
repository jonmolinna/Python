from abc import ABC, abstractclassmethod

class Vehiculo(ABC):
    @abstractclassmethod
    def ir(self):
        pass

class Coche(Vehiculo):
    def ir(self):
        print('Conduces el Auto')

class Motocicleta(Vehiculo):
    def ir(self):
        print('Andas en la moto')

coche = Coche()
coche.ir()