#Učitati datoteku json.example1 i izdvojiti punu adresu dostave paketa, ispisati jedno ispod drugog u txt datoteku adresa dostave
import json
{ "name"   : "John Smith",
  "sku"    : "20223",
  "price"  : 23.95,
  "shipTo" : { "name" : "Jane Smith",
               "address" : "123 Maple Street",
               "city" : "Pretendville",
               "state" : "NY",
               "zip"   : "12345" },
  "billTo" : { "name" : "John Smith",
               "address" : "123 Maple Street",
               "city" : "Pretendville",
               "state" : "NY",
               "zip"   : "12345" }


}

try:
    with open('C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/m3_03_datoteke/json_example1.json', 'r') as file_reader:
        dict_json=json.load(file_reader)

except Exception as e:
    print(f'Pogreška: {e}')

print(dict_json)

ime=dict_json["shipTo"]["name"]
ulica=dict_json["shipTo"]["address"]
grad=dict_json["shipTo"]["city"]
drzava=dict_json["shipTo"]["state"]
postanski_broj=dict_json["shipTo"]["zip"]

try:
    file_writer=open("C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/m3_03_datoteke/adresa_dostave.txt", "a")
    adresa_dostave=f'Adresa dostave je: \n{ime}\n{ulica}\n{grad}\n{drzava}\n{postanski_broj}'
    file_writer.write(adresa_dostave)

except Exception as e:
    print(f"Dgodila se pogreška {e}")



