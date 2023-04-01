import requests
from bs4 import BeautifulSoup

url = 'https://coreyms.com/'

stranica = requests.get(url).text

#print (stranica)

stranica_soup = BeautifulSoup (stranica)
#print (stranica_soup.prettify())

