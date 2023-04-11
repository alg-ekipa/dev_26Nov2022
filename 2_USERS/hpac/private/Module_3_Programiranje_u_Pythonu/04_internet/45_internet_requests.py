import requests
import json

url = 'https://www.bug.hr'

resp = requests.get(url)

#print(resp.status_code) - provjera pristupa, ako je 200 onda je OK

sadrzaj = resp.content
sadrzaj_dekodiran = sadrzaj.decode('UTF-8')

print(sadrzaj_dekodiran)

try:
    with open('C:/Users/Korisnik/Desktop/H/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/04_internet/bugweb.json','w') as file_writer:
        json.dump(sadrzaj_dekodiran, file_writer)

except Exception as e:
    print(' Došlo je do pogreške!!',e)