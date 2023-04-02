import requests
from bs4 import  BeautifulSoup

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
print(f'Ukupna populacija iznosi {sum(lista_populacija)}')
print()

povrsina=stranica_soup.select('.country-area')
#print(povrsina)
lista_povrsina=[]
for p in povrsina:
    lista_povrsina.append(float(p.text))
print(lista_povrsina)
print(f'Ukupna površina iznosi {sum(lista_povrsina)} km2')

# TO DO:

# 1. izračunati ukupnu populaciju i površinu svih država svijeta

# 2. izraditi rječnik oblika:
#       {'Andorra': ['Andorra la Vella', 84000, 468.0],
#           itd. }
# spremiti taj rječnik u json datoteku

rjecnik={}
lista_drzava=[]
lista_gradova=[]
drzava=stranica_soup.select('.country-name')
for i in drzava:
    lista_drzava.append(i.text.strip())
print(lista_drzava)

grad=stranica_soup.select('.country-capital')
for i in grad:
    lista_gradova.append(i.text.strip())
print(lista_gradova)

for i in range(len(lista_drzava)):
    kljuc = lista_drzava[i]
    grad_ = lista_gradova[i]
    rjecnik[kljuc] = grad_


for j in lista_populacija:
    rjecnik.values







# 3. izraditi klasu Drzava sa svojstvima glavni_grad, populacija, povrsina i instancirati objekte iz rječnika / datoteke '''