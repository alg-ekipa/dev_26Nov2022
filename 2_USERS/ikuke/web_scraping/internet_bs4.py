import requests
from bs4 import BeautifulSoup


url='https://www.scrapethissite.com/pages/simple'


stranica= requests.get(url).text

stranica_soup=BeautifulSoup(stranica)
print(stranica_soup.prettify())

populacija= stranica_soup.select('.country-population')


lista_populacija = []
for broj in populacija:
    lista_populacija.append(int(broj.text))

print(lista_populacija)


#TO DO

#izračunati ukupnu populaciju i površinu svih država svijeta

#IZRADITI RJEČNIK OBLIKA :

# {'Andorra':['Andora la Vella', 84000, 468.0]
#    itd. }
#spremiti taj rječnik u JSON datoteku


#izraditi klasu Država sa svojstvima glavni grad, populacija, površina i objekta iz rječnika/datoteka

"""

html_kod = '<p>Some<b>bad<i>HTML'

html_soup = BeautifulSoup(html_kod)

print(html_soup.prettify())

print(html_soup.find(text='bad'))

print(html_soup.p.b.i.text)

"""