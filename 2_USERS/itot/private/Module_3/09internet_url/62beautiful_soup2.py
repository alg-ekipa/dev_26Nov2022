from bs4 import BeautifulSoup
file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/09internet_url/62beautiful_soup2.json'

with open (file_path) as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

#print(soup) #test print dobije se ispis dokumenta

article = soup.find_all('div', class_='article')

#print(article) #test print

lista_brojeva = []
for a in article:
    print(a.text)
    lista_brojeva.append(float(a).strip()) # zbrajanje brojeva

print(lista_brojeva)




