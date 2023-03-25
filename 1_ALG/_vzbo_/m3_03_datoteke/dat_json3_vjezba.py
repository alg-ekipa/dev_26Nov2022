# Učitati datoteku json_example1 i izdvojiti punu adresu dostave paketa, ispisati jedno ispod drugog u txt datoteku adresa dostave

import json

dict_json = {}

try:
    with open('C:/Users/grafika10/Downloads/Datoteke/Datoteke/json_example1.json', 'r') as file_reader:
        dict_json = json.load(file_reader)
except Exception as e:
    print(f'Pogreška: {e}')

print(dict_json)

ime = dict_json["shipTo"]["name"]
ulica = dict_json["shipTo"]["address"]
grad = dict_json["shipTo"]["city"]
drzava = dict_json["shipTo"]["state"]
broj = dict_json["shipTo"]["zip"]

try: 
    file_writer = open("D:/Vesna/dev_26Nov2022/dev_26Nov2022/1_ALG/_vzbo_/m3_03_datoteke/adresa_dostave.txt", "a")
    adresa_dostave = f'Adresa dostave je:\n{ime}\n{ulica}\n{grad}\n{drzava}\n{broj}'
    file_writer.write(adresa_dostave)

except Exception as e:
    print(f"Dogodila se pogreska {e}")
