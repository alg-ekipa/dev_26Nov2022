from bs4 import BeautifulSoup

with open('C:/Users/Korisnik/Desktop/H/dev_26Nov2022/2_USERS/hpac/primjer.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

#print(soup)

article = soup.findAll('div',class_='article')

#print(article)

for a in article:
    print(a.text)

#print(article[0].text)

lista_brojeva = []
for a in article:
    #s = a.text
    #novi_s = float(s.strip())
    #lista_brojeva.append(float(s.strip()))
    lista_brojeva.append(float(a.text.strip()))

print(lista_brojeva)

print(sum(lista_brojeva)/len(lista_brojeva))
