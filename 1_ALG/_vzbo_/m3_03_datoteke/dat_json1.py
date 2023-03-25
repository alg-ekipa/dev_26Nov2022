import json

# podaci u obliku rječnika koje pohranjujemo u json datoteku
user = {
            "id": 1,
            "firstName": "Petar Peric",
            "lastName": "Petar Peric",
            "username": "pperic",
            "email": "pperic@email.adresa",
            "address": {
                "street": "Ilica 256",
                "city": "Zagreb",
                "zipcode": "10000"
            },
            "phone": "+385 1 8031 564",
            "website": "web.adresa",
            "company": {
                "name": "Medvednica d.o.o.",
                "catchPhrase": "Razvoj specijaliziranih Python aplikacija",
                "bs": "Najbolja poslovna rjesenja"
            }
        }

# upisivanje u json datoteku - metoda json.dump

try:
    with open('D:/Vesna/dev_26Nov2022/dev_26Nov2022/1_ALG/_vzbo_/m3_03_datoteke/user1.json', 'w') as file_writer:
        json.dump(user, file_writer, indent=4)

except Exception as e:
    print(f'Pogreška: {e}')

