class Animal:
    vivo = True

    def comer(self):
        print('Esta comiendo')

    def dormir(self):
        print('Esta dormiendo')

class Conejo(Animal):
    def correr(self):
        print('Corriendo')

class Pez(Animal):
    def nadar(self):
        print('Nadando')

class Halcon(Animal):
    def volar(self):
        print('Volando')

conejo = Conejo()
conejo.dormir()