import json

tekst_json = ''

#čitanje kao tekstualne datoteke (.txt) i spremanje u string
try:
    with open ('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/user1.json', 'r') as file_reader:
        tekst_json = file_reader

except Exception as ex:
    print (f'Pogreška: {ex}')

#pretvaranje stringa u json objekt (rječnik) pomoću metode json.loads
dict_json = json.loads(tekst_json)
#print(dict_json)

#čitanja direktno u rječnik pomoću metode json.load
dict_json = {}

try:
    with open ('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/user1.json', 'r') as file_reader:
        tekst_json = file_reader

except Exception as ex:
    print (f'Pogreška: {ex}')

print (dict_json)