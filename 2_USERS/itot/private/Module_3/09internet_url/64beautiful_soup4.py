import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'

stranica = requests.get(url).text # izvuce tekst iz stranice
#print(stranica) # ispisuje tekst sranice

stranica_soup = BeautifulSoup(stranica) # uljepsavamo stranicu sa BS
#print(stranica_soup.prettify())

populacija = stranica_soup.select('.country-population')  # trazi po elementu
#print(populacija)

lista_populacija = []
for broj in populacija:  #dodavanje trazenog u listu
    lista_populacija.append(int(broj.text))

print(lista_populacija) # ispis liste
'''
TODO: 
izraditi rijecnik obika:
  'Andorra' : [ 'Andorra la Vella', 84000, 468.0]
spremiti rijecnik u jsnon datoteku

izraditi klasu drzava sa svojstvima glavni grad, populacija, povrsina i instancirati objekte iz rijecnika / datoteke
'''

file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/09internet_url/64beautiful_soup4.json'
