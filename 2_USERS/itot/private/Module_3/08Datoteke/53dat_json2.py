#citanje u json datoteku

import json
file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/52dat_json1.json'

tekst_json = ''

try:
    with open (file_path, 'r') as file_reader:
        tekst_json = file_reader.read()

except Exception as e:
    print(f'Pogreska: {e}')

#print(tekst_json)
dict_json = json.loads(tekst_json)
print(dict_json)

dict_json = {}
try:
    with open(file_path, 'r') as file_reader:
        dict_json = json.load(file_reader)
except Exception as e:
    print(f'Pogreska: {e}')
print(dict_json)


