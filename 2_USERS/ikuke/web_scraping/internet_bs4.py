import requests
from bs4 import BeautifulSoup


url='https://www.scrapethissite.com/pages/simple'


stranica= requests.get(url).text

stranica_soup=BeautifulSoup(stranica)
print(stranica_soup.prettify())

populacija= stranica_soup.select('.country-population')
imena_zemalja=stranica_soup.select('.country-name')









ukupan_broj=0

lista_populacija = []
for broj in populacija:
    ukupan_broj+=int(broj.text)
    lista_populacija.append(int(broj.text))


lista_zemalja = []
for ime in imena_zemalja:
    zemlja=ime.text
    zemlja=zemlja.replace('\n','')
    print(zemlja)
    lista_zemalja.append(ime.text)







rjecnik_iz_liste2 = {}

lista_kljuceva = [1, 2, 3, 4, 5]
lista_vrijednosti = ['python', 'c++', 'java', 'perl', 'asp.net']

for i in range (len(lista_kljuceva)):
    kljuc=lista_kljuceva[i]
    print ('ključ---------------->', kljuc)
    vrijednost=input ('Unesi vrijednost-->')

    rjecnik_iz_liste2[kljuc]=vrijednost


for k, v in rjecnik_iz_liste.items():
    print(f'{k} : {v}')


for k, v in rjecnik_iz_liste2.items():
    print(f'{k} : {v}')







#print(lista_populacija)
print('ukupan broj ljudi je: ', ukupan_broj)

print('ukupan broj ljudi je: ', ukupan_broj//1000000000, (ukupan_broj%1000000000)//1000000, ((ukupan_broj%1000000000)//1000)%1000, ukupan_broj%1000)

#print(lista_zemalja)
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