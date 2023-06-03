from bs4 import BeautifulSoup

with open ('C:/Users/Korisnik/Desktop/26.11/dev_26Nov2022/2_USERS/zbene/private/Module_3/01.04.2023/primjer.html') as html_file:
    soup = BeautifulSoup (html_file, 'html.parser')

#print (soup)

article = soup.find_all ('div', class_='article')

#print (article)

lista_brojeva = []

for a in article:
    #s = a.text
    #novi_s = float (s.strip())
    lista_brojeva.append (float(a.text.strip()))
    
print (sum(lista_brojeva)/len(lista_brojeva))