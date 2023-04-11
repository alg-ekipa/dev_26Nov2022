import requests
import json

file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/09internet_url/60internet_requests2.json'

url = 'https://www.bug.hr'  #izbor stranice

resp = requests.get(url)   # citamo url
print(resp.status_code)  # provjera odobrenja pristupa, ako je 200 onda je OK

sadrzaj = resp.content
sadrzaj_dekodiran = sadrzaj.decode('utf-8') 

print(sadrzaj_dekodiran)  #sada samo dobili sadtzaj u ispisu koji je citljiviji

try:
    with open(file_path, 'w') as file_weiter:
        json.dump(sadrzaj_dekodiran,file_weiter)

except Exception as e:
    print(f'došlo je do pogreške {e}')

    # TODO: neku grešku baca