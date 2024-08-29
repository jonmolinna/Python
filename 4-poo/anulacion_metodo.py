class Animal:
    def comer(self):
        print('Este animal esta comiendo')

class Conejo(Animal):
    def comer(self):
        print('Este conejo esta comiendo una Zanahoria')

conejo = Conejo()

conejo.comer()