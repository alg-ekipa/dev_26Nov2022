import requests
from bs4 import BeautifulSoup

url = 'https://coreyms.com/'

stranica = requests.get(url).text

#print (stranica)

stranica_soup = BeautifulSoup (stranica)
#print (stranica_soup.prettify())

article = stranica_soup.find ('article') #traži po elementu
#print (article)

tekst = article.find('div', class_='entry-content').p.text
print (tekst)