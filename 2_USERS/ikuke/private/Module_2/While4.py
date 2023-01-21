"""while True:
    broj = int(input("Unesite broj u rasponu od 10 do 20: "))
    if 10 <= broj  <= 20:
        print("Uspješan unos.")
        break
    else:
        print("broj nije u zadanom rasponu, pokušajte ponovo.")
 

password = "tajno"
while True:
    unos = input("Unosi password: ")
    if unos == password:
          print("Točno.")
          break
    else:
        print("Krivi password, pokušajte ponovo.")
"""

while True:
    unos = input("Unesite broj u rasponu od 10 do 20: ")

    while unos.isdigit() == False:
        print("Krivi unos, morate unjeti broj. Ponovite unos. ")
        unos = input("Unesite broj u rasponu od 10  do 20.")
    if int(unos) >= 10 and int(unos) <= 20:
        print("Uspješan unos.")
        break

    else:
        print("Broj nije u zadanom rasponu, pokušajte ponovo.")