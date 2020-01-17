# -*- coding: utf-8 -*-
import random
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |''','''
        
    +---+
    |   |
    O   |
        |
        |
        |
        ''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
        ''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        ''','''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ''','''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        ''','''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        
''']
peliculas=[
    'harry_potter',
    'avatar',
    'titanic',
    'prety_woman',
    'amelie',
    'dia_de_la_independencia',
    'matrix',
    'kill_bill',
    'brave_hearth',
    'la_bruja_de_blair'
]

videojuegos=[
    'the_legend_of_celda',
    'gta_san_adreas',
    'super_mario',
    'red_dead_redemption',
    'metroid_prime',
    'halo',
    'bioshock',
    'doom',
    'unchearted',
    'resident_evil'
]

distribuciones_linux=[
    'mint',
    'ubuntu',
    'debian',
    'fedora',
    'red_hat',
    'artegos',
    'zoris',
    'manjaro',
    'opensuse',
    'solus'
]

palabras = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

letters =[]

def random_word():
    idx = random.randint(0, len(palabras) - 1)
    return palabras[idx]

   

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    opcion = 1

    while opcion == 1:
        while True:
            display_board(hidden_word, tries)
            current_letter = str(input('Escoge una letra: '))
                
            letter_indexes = []
            for idx in range(len(word)):
                if word[idx] == current_letter:
                    letter_indexes.append(idx)
            

            if len(letter_indexes) == 0:
                
                if current_letter in letters:
                    print(' YA PUSISTE ESA LETRA')
                    tries=tries
                else:
                    letters.append(current_letter)
                    tries += 1
                if tries == 7:
                    display_board(hidden_word, tries)
                    print('')
                    print('¡Perdiste! La palabra correcta era {}'.format(word))
                    break
            else:
                for idx in letter_indexes:
                    hidden_word[idx] = current_letter

                letter_indexes = []

            try:
                hidden_word.index('-')
            except ValueError:
                print('')
                print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
                break
        opcion == print(input('Si quieres seguir jugando pulsa 1 de lo contrario pulsa 2: '))
        opcion=int(opcion)
    

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    opcion = input('oprime 1 si quieres jugar o 2 si quieres salir ')
    opcion=int(opcion)
    if opcion == 1:
        run()

    elif opcion > 2:
        print('esta opcion no es valida')

    else:
        print('Game Over')
