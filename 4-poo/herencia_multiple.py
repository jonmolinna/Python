class Presa:
    def huir(self):
        print('Este animal huye')

class Depredador:
    def cazar(self):
        print('Este animal esta cazando')

class Conejo(Presa):
    pass

class Halcon(Depredador):
    pass

class Pez(Presa, Depredador):
    pass