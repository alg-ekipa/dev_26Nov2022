import requests
import json

url = 'https://www.bug.hr'

resp = requests.get(url) # u get se može odmah staviti string

# print(resp.status_code) provjera jeli status odobren

# Uzet ćemo sadržaj i dekodirati ga

sadrzaj = resp.content
sadrzaj_dekodiran = sadrzaj.decode('utf-8')

print(sadrzaj_dekodiran)

# doili smo sadržaj, idemo ga staviti u datoteku 

try: 
    with open('bugweb.json', 'w') as file_writer: 
        json.dump(sadrzaj_dekodiran, file_writer)

except Exception as e: 
    print('Došlo je do pogreške!', e)

# uhvatili smo sve u datoteku 



