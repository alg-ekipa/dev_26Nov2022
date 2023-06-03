#Učitati datoteku json_example1 i izdvojiti punu adresau dostave paketa, ispisati jedno ispod drugog u txt datoteku adresa dostave

import json

dict_json = {}

try:
    with open ('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/json.example.json', 'r') as file_reader:
        dict_json = json.load(file_reader)

except Exception as ex:
    print(f'Pogreška: {ex}')

print(dict_json)

ime = dict_json["shipTo"]["name"]
ulica = dict_json["shipTo"]["address"]
grad = dict_json["shipTo"]["city"]
drzava = dict_json["shipTo"]["state"]
broj = dict_json["shipTo"]["zip"]

try: 
    file_writer = open('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/json.example.json', "a")
    adresa_dostave = f'Adresa dostave je:\n{ime}\n{ulica}\n{grad}\n{drzava}\n{broj}'
    file_writer.write(adresa_dostave)

except Exception as ex:
    print(f"Dogodila se pogreška {ex}")