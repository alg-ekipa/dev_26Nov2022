import json

#Podaci u obliku rječnika koje pohranjujemo u json datoteku
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

try:
    with open ('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/user1.json', 'w') as file_writer:
        json.dump(user, file_writer)

except Exception as ex:
    print (f'Pogreška: {ex}')