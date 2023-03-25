# Učitati datoteku json_example1 i izdvojiti punu adresu dostave paketa, ispisati jedno ispod drugog u txt datoteku adresa dostave

import json
file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/54json_example1.json'
file_write_path= 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/54shipping_adress.txt'
trazeni_key= "shipTo" 

dict_json = {}
try:
    with open(file_path, 'r') as file_reader:
        dict_json = json.load(file_reader)
except Exception as e:
    print(f'Pogreska: {e}')

dict_adresa = dict_json[trazeni_key]   # pretvara iz rijecnika po keyu, u novi rijecnik

for x,y in dict_adresa.items():
    file_writer = open(file_write_path, "a")
    file_writer.write(f'{str(x)} {str(y)}\n')
    file_writer.close()

 
