import requests
from bs4 import BeautifulSoup

url = 'https://coreyms.com/'

stranica = requests.get(url).text # izvuce tekst iz stranice
#print(stranica) # ispisuje tekst sranice

stranica_soup = BeautifulSoup(stranica) # uljepsavamo stranicu sa BS
#print(stranica_soup.prettify())

article = stranica_soup.find('article')  # trazi po elementu
#print(article)

tekst = article.find('div', class_="entry-content").p.text # micanje tagova
#print(tekst)

video = article.find('iframe', class_='youtube-player') #nalazi video

print(video['src'])

link = video['src']
link_odvoji = link.split('/')
print(link_odvoji[4].split('?')[0])

