import requests
import json

url = 'https://www.bug.hr'

resp = requests.get(url)

#print (resp.status_code) -- pristup nam je odobren

sadržaj = resp.content
sadržaj_dekodiran = sadržaj.decode('utf-8')

print (sadržaj_dekodiran)

try:
    with open ('C:/Users/Korisnik/Desktop/26.11/dev_26Nov2022/2_USERS/zbene/private/Module_3/01.04.2023/bugweb.json', 'w') as file_writer:
        json.dump(sadržaj_dekodiran, file_writer)

except Exception as ex:
    print ('Došlo je do pogreške!', ex)