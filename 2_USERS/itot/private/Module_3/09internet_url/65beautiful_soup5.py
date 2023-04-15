'''S navedene stranice izdvojite sve odlomke (tekstove) i spremite u txt datoteku. 
Izdvojite kontakt (e-mail i broj mobitela) prikažite ih na zaslonu '''

import requests
from bs4 import BeautifulSoup

file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/09internet_url/65beautiful_soup5.txt'
url = 'https://www.klubsumica.com/manje-privatne-zabave/'

stranica = requests.get(url).text 
stranica_soup = BeautifulSoup(stranica)

article = stranica_soup.find('p')  # nadje samo jedan

'''Spremanje odlomaka u txt'''
article2 = stranica_soup.find_all('p') # nadje sve i stavi u listu, pa mora preko petlje ispis
for broj in article2:  #ispis articla, jer su u listi
  try: 
    with open(file_path, "a", encoding="utf-8") as fil3: # encoding="utf-8" jer moramo kodirati stvar koju upisujemo
      fil3.write(broj.text+"\n") # "\n" da svaki paragraf ide u novi red

  except Exception as e:
    print(f'Pogreška: {e}')

''' ispis maila sa stranice'''
mail_kontakt = stranica_soup.find_all('a')
for mail in mail_kontakt:  #prolaz kroz sve zapise 
  if '@' in mail.text:
    print(f'Kontakt email je: {mail.text}')
 

''' ispis kontakt broja sa stranice'''
broj_kontakt = stranica_soup.find_all('strong')
for broj in broj_kontakt:  ##prolaz kroz sve zapise 
  if '09' in broj.text:
    print(f'Kontak broj je:: {broj.text}')

