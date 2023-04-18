import json

tekst_json = ''

#čitanje kao teksutalnu datoteku (.txt) - i spreanje u string
try:
    with open ('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/user1.json', 'r') as file_reaader:
        tekst_json = file_reaader.read()

except Exception as e:
    print(f'Pogreška : {e}')

print(tekst_json)

#pretvaranje stringa u json objekt (rječnik) pomoću metode json.loads
dict_json = json.loads(tekst_json)
print(dict_json)

# čitanje direktno u rječnik pomoću metode json.load

dict_json = {}

try:
    with open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/user1.json', 'r') as file_reaader:
        dict_json = json.load(file_reaader)
except Exception as e:
    print(f'Pogreška : {e}') 

print(dict_json)