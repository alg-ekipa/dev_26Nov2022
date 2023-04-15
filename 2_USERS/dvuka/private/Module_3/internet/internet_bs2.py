from bs4 import BeautifulSoup

with open('C:/Users/Korisnik/Desktop/dev_26Nov2022/2_USERS/dvuka/private/Module_3/primjer.html') as html_file:
    soup=BeautifulSoup(html_file, 'html.parser')

#print(soup)

article=soup.findAll('div', class_='article')

#print(article)

lista_brojeva=[]
for a in article:
    #s=a.text
    #novi_s=float(s.strip())
    lista_brojeva.append(float(a.txt.strip()))

print(sum(lista_brojeva)/len(lista_brojeva))

#print(article[0].text)

