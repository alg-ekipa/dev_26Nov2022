from bs4 import BeautifulSoup

with open ('primjer.html') as html_file:

        soup = BeautifulSoup(html_file,'html.parser')

#print(soup)


article = soup.find_all('div', class_='article')

print(article)

lista_brojeva = []
for a in article:
    lista_brojeva.append(a.text)

print(lista_brojeva)




"""
html_kod = '<p>Some<b>bad<i>HTML'

html_soup = BeautifulSoup(html_kod)

print(html_soup.prettify())

print(html_soup.find(text='bad'))

print(html_soup.p.b.i.text)

"""