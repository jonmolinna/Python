class Coche:
    color = None

def change_color(coche, color):
    coche.color = color

coche1 = Coche()
coche2 = Coche()
coche3 = Coche()

change_color(coche1, 'rojo')
change_color(coche2, 'azul')
change_color(coche3, 'blanco')

print(coche1.color)
print(coche2.color)
print(coche3.color)