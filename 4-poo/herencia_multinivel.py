class Organismo:
    vivo = True

class Animal(Organismo):
    def comer(self):
        print('Este animal esta comiendo...')

class Perro(Animal):
    def ladrar(self):
        print('Este perro esta ladrando...')

perro = Perro()

print(perro.vivo)