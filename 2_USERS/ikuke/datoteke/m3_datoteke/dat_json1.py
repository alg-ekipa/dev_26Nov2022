import os
import platform

def vrati_putanju(datoteka):
    os.system('cls')
    absolute_path = os.path.dirname(__file__)
    print(absolute_path)
    putanja=""
    if platform.system() == "Windows":
        print("operacijski sustav Windows")
    i=len(absolute_path)
    for k in range (i):
        slovo=absolute_path[k]
        if slovo == "\\" :
            putanja=putanja+"/"
        else:
            putanja=putanja+slovo
    putanja=putanja+"/"

    print (absolute_path)
    print (putanja+datoteka)
    #input()

    return putanja+datoteka



file1=vrati_putanju("user1.json")
import json

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
    with open (file1,'w') as file_writer:
        json.dump(user,file_writer, indent=4)

except Exception as e:
    print ('desila se pogreška')