import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'

stranica = requests.get(url).text

stranica_soup = BeautifulSoup(stranica)
print(stranica_soup.prettify())

populacija = stranica_soup.select('.country-population')
#print(populacija)

lista_populacija = []
for broj in populacija:
    lista_populacija.append(int(broj.text))

print(lista_populacija)

# Za učiniti:
# Izraditi rječnik oblika: 
#       {'država':['glavni grad','broj stanovnika','površina']
#           itd...}

# Spremiti taj tječnik u json datoteku

# Izračunati ukupnu populaciju i porvšinu svih zemalja

# Izraditi klasu Država sa svojstvima glavni_grad, populacija površina i instancirati objekte iz rječnika/datoteke 