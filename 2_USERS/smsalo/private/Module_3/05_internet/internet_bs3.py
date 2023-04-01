import requests
from internet_bs4 import BeautifulSoup


url='https://coreyms.com/'
stranica=requests.get(url).text
#print(stranica)

#sad ju treba uljepšati za čitanje/obradu

stranica_soup=BeautifulSoup(stranica)
print(stranica_soup.prettify())

article=stranica_soup.find('article')       #traži po elementu koji stavimo u ''  'article' 'p' 
print(article)
print()

tekst=article.find('div', class_='entry-content').p.text
print(tekst)
print()

yt_video=article.find('iframe', class_='youtube-player')        #unutar articla niže prema linku, svi su nesto=....; dohvatiti kao index [nesto]
link=yt_video['src']
print(link)

link_odvojeni=link.split('/')
print(link_odvojeni)
print(link_odvojeni[4].split('?')[0])

