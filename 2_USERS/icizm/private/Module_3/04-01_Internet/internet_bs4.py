import requests 
from bs4 import BeautifulSoup 

url = 'https://www.scrapethissite.com/pages/simple/'

stranica = requests.get(url).text

#print(stranica)

stranica_soup = BeautifulSoup(stranica)
#print(stranica_soup.prettify())


lista_drzava = []

lista_population =  []
lista_povrsina = []

cotw = {}


populacija = stranica_soup.select('.country-population')
#print(populacija)

for broj in populacija: 
    lista_population.append(int(broj.text))

print('Zbroj populacije svih država je', sum(lista_population), 'ljudi')

print()

povrsina = stranica_soup.select('.country-area')


for broj in povrsina: 
    lista_povrsina.append(float(broj.text))

print('Zbroj površina svih država je', sum(lista_povrsina), 'km2')
print()


# kako sad odvojiti ime države???
drzave = stranica_soup.select('.country-name')

for d in drzave: 
    lista_drzava.append(d.text.strip()) # dodajem strip da mi očisti višak koda

print(lista_drzava)
print()


lista_gradova = []
gradovi = stranica_soup.select('.country-capital')

for g in gradovi: 
    lista_gradova.append(g.text) 

print(lista_gradova)



# TO DO! 

# izračunati ukupnu populaciju i površinu svih država svijeta

# izraditi riječnik oblika: 
# {'Andorra' : ['Andora la Vella', 84000, 468.0], 
# }
# spremiti taj riječnik u json datoteku

# izraditi klasu država sa svojstvima glavni grad, populacija, površina i instancirati objekte iz riječnika / datoteke