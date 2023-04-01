#sa stranice https: https://www.klubsumica.com/manje-privatne-zabave/

from bs4 import BeautifulSoup
import requests

stranica = 'https://www.klubsumica.com/manje-privatne-zabave/'

podaci_sadržaj = requests.get(stranica).content
sadržaj = BeautifulSoup (podaci_sadržaj, 'html.parser')
#print (sadržaj)

kontakti = sadržaj.select ('.elementor-element-17e9151 ul li')

kontakt_podaci = []

