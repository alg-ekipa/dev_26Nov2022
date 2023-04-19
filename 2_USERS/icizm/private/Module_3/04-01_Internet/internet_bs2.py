from bs4 import BeautifulSoup 

# najprije ćemo raditi sa lokalinim fajlom

with open('primjer.html') as html_file: 
    soup = BeautifulSoup(html_file) # može sadržavati i drugi argument html.parser ili xml

# print(soup) # dobijemo lijepo raspoređen html

# Želimo dohvatiti parametre

article = soup.find_all('div' , class_= "article") #class mora biti sa _ kao posebna varijabla

#print(article) #dobili smo listu

'''for a in article: 
    print(a)

#nema više liste ali smetaju tagovi'''

for a in article: 
    print(a.text)

# dobijemo samo tekst svih paragrafa

# print(article[0].text) dohvati samo prvi paragraf