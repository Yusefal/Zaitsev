# -*- coding: utf-8 -*- 

countries = {
    'mexico':122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru':31
}

while True:
    country = str(input('Escribe el pais del que deseas conoce la poblacion: ')).lower()
    try:
        print('la poblacion de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('no contamos con la poblacion de ese paìs')

