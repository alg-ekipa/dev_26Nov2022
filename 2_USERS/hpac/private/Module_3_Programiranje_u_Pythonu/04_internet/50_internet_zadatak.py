import requests
from bs4 import BeautifulSoup

stranica = 'https://www.klubsumica.com/manje-privatne-zabave/'

podaci_sadrzaj = requests.get(stranica).content

sadrzaj = BeautifulSoup(podaci_sadrzaj, 'html.parser')

kontakti = sadrzaj.select('.elementor-element-17e9151 ul li')

kontakt_podaci = []

for i in range(len(kontakti)):
    kontakt_podaci.append(kontakti[i].text)

    with open('C:/Users/Korisnik/Desktop/H/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/04_internet/kontakt_podaci.txt','w') as file_writer:
        for kontakt in kontakt_podaci:
            za_ispis = f'{kontakt}\n'
            file_writer.write(za_ispis)