import requests
from bs4 import BeautifulSoup

url='https://www.scrapethissite.com/pages/simple/'

stranica=requests.get(url).text

stranica_soup=BeautifulSoup(stranica)
#print(stranica_soup.prettify())

povrsina=stranica_soup.select('.country-area')
populacija=stranica_soup.select('.country-population')
#print(populacija)

lista_populacija=[]
for broj in populacija:
    lista_populacija.append(int(broj.text))

print(sum(lista_populacija))

lista_povrsina=[]
for broj in povrsina:
    lista_povrsina.append(float(broj.text))

print(sum(lista_povrsina))


#TO DO:
#Izračunati ukupnu populaciju i površinu svih država svijeta
#izraditi rječnik oblika:
#   {'Andorra':['Andorra la Vella', 84000, 468.0], itd.}
#spremiti taj rječnik u json datoteku

#izraditi klasu Država sa svojstvima glavni_grad, populacija, površina i i nstancirati objekte iz ječnika/datoteke