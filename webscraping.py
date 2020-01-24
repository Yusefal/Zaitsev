#web scraping 
# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import urllib

def run ():
    for i in rang (1,10):
        response = requests.get('https://xkcd.com/{}'.format(i)) #estudiar metodo get y post 
        soup = BeautifulSoup(response.content, 'html.paser')
        image_containe = soup.find(id='comic') #id del div en el html

        image_url = image.container.find('img')['src'] #Referencia de la imagen en el html
        image_name = image_url_split('/')[-1] #Url de referencia de la imagen , -1 indica que es el ultimo valor(para identificar el nombre)
        print('Descargando la imagen {}'.format(image_name))
        urllib.urlretrieve('https:{}'.format(imagen_url),image_name)

if __name__ == '__main__':
    run()
