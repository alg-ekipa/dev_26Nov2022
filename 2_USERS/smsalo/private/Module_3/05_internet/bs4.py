import requests
from bs4 import BeautifulSoup

adresa = 'https://www.scrapethissite.com/pages/simple/'
stranica = requests.get(adresa).text

stranica_soup=BeautifulSoup(stranica)
print(stranica_soup.prettify())
