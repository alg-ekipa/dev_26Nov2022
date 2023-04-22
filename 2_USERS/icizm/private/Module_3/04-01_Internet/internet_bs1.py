# Uvod da vidimo što je beautifulsoup

from bs4 import BeautifulSoup

# izrađujemo mini html kod

html_kod = '<p>Some<b>bad<i>HTML'

html_soup = BeautifulSoup(html_kod) 
# popravlja html kod, uljepšava

print(html_soup.prettify())


print(html_soup.find(text='bad')) # može pronaći određenu stvar

print(html_soup.p) # pronalaženje po tagu
print(html_soup.p.b.i.text) # hijerarhijski se spuštamo do točno određenog teksta