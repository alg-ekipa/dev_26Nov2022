import json

tekst_json= ''

#ČITANJE kao tekstalna datoteka

try:
    with open('user1.json', 'r') as file_reader:
        tekst_json=file_reader.read()

except Exception as e:
    print(f'Pogreška {e}')

print(tekst_json)

#pretvaranje stringa u json objekt(rječnik) pomoću metode json.loads
dict_json=json.loads(tekst_json)
print(dict_json)


#ČITANJE direktno u rječnik

d_json={}
try:
    with open('user1.json', 'r') as file_reader:
        d_json=json.load(file_reader)

except Exception as e:
    print(f'Pogreška {e}')

print(d_json)
