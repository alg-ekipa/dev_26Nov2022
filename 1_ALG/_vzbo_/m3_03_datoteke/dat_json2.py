import json

tekst_json = ''

# čitanje kao tekstualne datoteke (.txt) i spremanje u string
try:
    with open('D:/Vesna/dev_26Nov2022/dev_26Nov2022/1_ALG/_vzbo_/m3_03_datoteke/user1.json', 'r') as file_reader:
        tekst_json = file_reader.read()

except Exception as e:
    print(f'Pogreška: {e}')

# pretvaranje stringa u json objekt (rječnik) pomoću metode json.loads
dict_json = json.loads(tekst_json)
#print(dict_json)

# čitanje diretkno u rječnik pomoću metode json.load

dict_json = {}

try:
    with open('D:/Vesna/dev_26Nov2022/dev_26Nov2022/1_ALG/_vzbo_/m3_03_datoteke/user1.json', 'r') as file_reader:
        dict_json = json.load(file_reader)
except Exception as e:
    print(f'Pogreška: {e}')

print(dict_json)