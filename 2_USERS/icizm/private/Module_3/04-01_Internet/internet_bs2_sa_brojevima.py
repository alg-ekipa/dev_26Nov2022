from bs4 import BeautifulSoup 

# najprije ćemo raditi sa lokalinim fajlom

with open('primjer_brojevi.html') as html_file: 
    soup = BeautifulSoup(html_file) # može sadržavati i drugi argument html.parser ili xml

# print(soup) # dobijemo lijepo raspoređen html

# Želimo dohvatiti parametre

article = soup.find_all('div' , class_= "article") #class mora biti sa _ kao posebna varijabla

#print(article) #dobili smo listu

'''for a in article: 
    print(a)

#nema više liste ali smetaju tagovi'''

lista_brojeva = []

'''for a in article: 
    s = a.text                       #uzela da je s svaki taj član
    novi_s = float(s.strip())        #nad njime napravila strip i pretvorila ih u floatove
    lista_brojeva.append(novi_s) '''

for a in article: 
    lista_brojeva.append(float(a.text.strip()))

print(sum(lista_brojeva) / len(lista_brojeva)) #prosjek
