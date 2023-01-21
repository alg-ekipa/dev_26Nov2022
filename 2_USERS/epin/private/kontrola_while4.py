#Unos broja u nekom rasponu, npr. između 10 i 20
""" ---bez prvojere unosi li korisnik znak ili broj
while True:
    broj = int(input("Unesite broj u rasponu od 10 do 20: "))
    if 10 <= broj <= 20:
        print("Uspješan unos!")
        break
    else:
        print("Broj nije u zadanom rasponu, pokušajte ponovno")
"""

while True:
   unos = input("Unesite broj u rasponu od 10 do 20: ")
   
    while unos.isdigit() == False:
    print("Krivi unos! Morate unijeti BROJ! Ponovite unos!")
    unos = input("Unesite broj u rasponu od 10 do 20: ")
    if int(unos) >= 10 and int(unos) <= 20:
        print("Uspješan unos!")
        break

    else:
        print("Broj nije u zadanom rasponu, pokušajte ponovno")
    



#s ="123"
#print(s.isdigit())

