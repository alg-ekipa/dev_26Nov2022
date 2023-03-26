# Učitati datoteku json_example1 i izdvojiti punu adresu dostave paketa, ispisati jedno ispod drugog u txt datoteku adresa dostave

import json 

try:
    with open ('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/json_example1.json', 'r') as file_reaader:
        dict_json = json.load(file_reaader)

except Exception as e:
    print(f'Pogreška : {e}')

print(dict_json)
print(type(dict_json))

ime = dict_json['shipTo']['name']
adresa = dict_json['shipTo']['address']
grad = dict_json['shipTo']['city']
drzava = dict_json['shipTo']['state']
posta_br = dict_json['shipTo']['zip']


try:
    file_writer = open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/JsonAdresa.txt','a')
    redak = f'Dosaviti:\n{ime}\n{adresa}\n{grad}\n{drzava}\n{posta_br}'
    file_writer.write(redak)
except Exception as e:
    print(f'Pogreška : {e}')




