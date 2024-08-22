import random

lista = ['roca', 'papel', 'tijera']

while True:
    laptop = random.choice(lista)
    game = None

    while game not in lista:
        game = input('roca, papel o tijera?: ').lower()

    if game == laptop:
        print('Laptop: ', laptop)
        print('Jugador: ', game)
        print('Empate!')

    elif game == 'roca':
        if laptop == 'papel':
            print('Laptop: ', laptop)
            print('Jugador: ', game)
            print('Perdiste!')
        if laptop == 'tijera':
            print('Laptop: ', laptop)
            print('Jugador: ', game)
            print('Ganaste!')

    elif game == 'papel':
        if laptop == 'tijera':
            print('Laptop: ', laptop)
            print('Jugador: ', game)
            print('Perdiste!')
        if laptop == 'roca':
            print('Laptop: ', laptop)
            print('Jugador: ', game)
            print('Ganaste!')

    elif game == 'tijera':
        if laptop == 'roca':
            print('Laptop: ', laptop)
            print('Jugador: ', game)
            print('Perdiste!')
        if laptop == 'papel':
            print('Laptop: ', laptop)
            print('Jugador: ', game)
            print('Ganaste!')

    newPlay = input('Quieres jugar de nuevo? (si/no): ').lower()

    if newPlay != 'si':
        break