import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.scrapethissite.com/pages/simple/'

stranica = requests.get(url).text

stranica_soup = BeautifulSoup(stranica, 'html.parser')
#print(stranica_soup)



#Izračunati ukupnu populaciju 
populacija =stranica_soup.select('.country-population')
lista_populacija = []
for broj in populacija:
    lista_populacija.append(int(broj.text))
print(f'Ukupno stanovnistvo je: {sum(lista_populacija)}')

#površinu svih država svijeta
povrsina = stranica_soup.select('.country-area')
lista_povrsina = []
for pov in povrsina:
    lista_povrsina.append(float(broj.text))
print(f'Ukupna povrsina iznosi: {sum(lista_povrsina)} km2')


# Izraditi riječnik

data = {}
data['drzava'] = [element.text for element in stranica_soup.select(".country-name")]
data['gl_grad'] = [element.text for element in stranica_soup.select(".country-capital")]
data['populacija'] =  [element.text for element in stranica_soup.select(".country-population")]
data['velicina'] =  [element.text for element in stranica_soup.select(".country-area")]


countries = []
# zip() funkicja 
for country, capital, population, area in zip(stranica_soup.select(".country-name"), stranica_soup.select(".country-capital"), stranica_soup.select(".country-population"), stranica_soup.select(".country-area")):
    countries.append({
        'drzava': country.text.replace('\n', '').strip(),
        'gl_grad': capital.text,
        'populacija': population.text,
        'velicina': area.text
    })

try:
    with open('drzave.json', 'w', encoding='utf-8') as file_writer:
        json.dump(countries, file_writer, indent=4, ensure_ascii=False)

except Exception as e:
    print(f'Greška: {e}')
