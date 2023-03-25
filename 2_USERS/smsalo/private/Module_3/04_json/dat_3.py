#Učitati datoteku json_example1 i izdvojiti punu adresu dostave paketa, ispisati jedno ispod drugog i txt datoteku adresu dostave

import json


d_json={}

try:
    with open('json_example1.json', 'r') as file_reader:
        d_json=json.load(file_reader)

except Exception as e:
    print(f'Pogreška {e}')

ime= d_json['shipTo']['name']
adresa=d_json['shipTo']["address"]
grad=d_json['shipTo']["city"]
drzava=d_json['shipTo']["state"]
zip=d_json['shipTo']["zip"]
 
try:
    with open('adresa.txt', 'a') as file_writer:
        opis=f'{ime}\n{adresa}\n{grad}\n{drzava}\n{zip}'
        file_writer.write(opis)
except Exception as e:
    print(f'Pogreška {e}')