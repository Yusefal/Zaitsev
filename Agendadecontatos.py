# -*- coding: utf-8 -*-


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Agenda:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        print('name: {}, phone: {}, email: {}'.format(name, phone, email))

def run():

    contact_book = Agenda()
    while True:
        command = str(input('''
        ¿Que deseas hacer? 
        
        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        '''))

        if command == 'a':
            print ('anadir contacto')
            name = (str(input('Escribe el nombre del contacto: ')))
            phone = (str(input('Escribe el numero del contacto: ')))
            email = (str(input('Escribe el email del contacto: ')))
            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            print('Buscar contacto')

        elif command == 'e':
            print ('Eliminar Contacto')

        elif command == 'l':
            print ('lista de contactos')

        elif command =='s':
            break
        else:
            print('Comando no encontrado')

if __name__ == '__main__':
    run ()

            