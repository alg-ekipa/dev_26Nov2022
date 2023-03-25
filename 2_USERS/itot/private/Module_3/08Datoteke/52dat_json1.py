#upisivanje u json datoteku

import json
file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/52dat_json1.json'

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
    with open(file_path, 'w') as file_writer:
        json.dump(user, file_writer, indent=4)

except Exception as e:
    print(f'Pogreška: {e}')
