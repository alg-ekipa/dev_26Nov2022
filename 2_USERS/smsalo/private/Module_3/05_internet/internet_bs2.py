from internet_bs4 import BeautifulSoup


with open('primjer.html') as html_file:
    soup=BeautifulSoup(html_file, 'html.parser')

#print(soup)

article=soup.find_all('div', class_='article')

print(article)
for a in article:
    print(a.text)

print(article[0].text)

lista_brojeva=[]
for a in article:
    lista_brojeva.append(a.text)

print(lista_brojeva)

lista_br=[]                     #može se spojiti na gornju listu tako da je b=a.text c=float(b.strip()) ....
for a in lista_brojeva:
    a=float(a.strip())
    lista_br.append(a)

print(lista_br)
print(sum(lista_br)/len(lista_br))






