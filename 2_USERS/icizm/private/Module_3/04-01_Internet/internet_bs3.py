import requests 
from bs4 import BeautifulSoup 

url = 'https://coreyms.com/ '

stranica = requests.get(url).text

#print(stranica)

stranica_soup = BeautifulSoup(stranica)
#print(stranica_soup.prettify())

article = stranica_soup.find('article') # traži po elementu, u navodneike pod stringom moramo staviti odgovarajući element
#print(article)

''' div tagovi sadrže class'''

tekst = article.find('div', class_='entry-content').p.text # izvlačimo varijablu da možemo spremiti u neku datoteku kasnije

#print(tekst)

video = article.find('iframe', class_= 'youtube-player')

print(video['src']) #kao po ključu od riječnika tražimo ono što definira link - src u ovom slučaju i onda nam izdvoji taj youtube link

# ako bi htjeli izvaditi kod videa kako doći do njega?
# splitanje na slashu? 

link = video['src']
link_split = link.split('/') # odvojili smo youtube link po /
print(link_split[4].split('?')[0]) # odvojili opet sa ? jer sa njim završava kod koji nam treba u 4. djelu koji je odvojen sa / pa onda stavljamo 0 jer je to prvi upitnik u linku pa uzimamo prvi dio