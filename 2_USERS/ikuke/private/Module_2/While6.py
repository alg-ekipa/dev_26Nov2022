#TO DO
#Unos stringa
#Raspon brojeva
#Nova igra

import random

zamisljeni_broj = random.randint(1,50)

brojac = 0
igra = 1

while igra:
    unos_broja = str(input("Pogodi broj: "))
    isdigit = unos_broja.isdigit()
    if isdigit == True:
        if int(unos_broja)>zamisljeni_broj:
            brojac += 1
            print("Broj je manji od unešenog!")
            print(brojac, ".  pokušaj", sep = "")
        elif int(unos_broja)<zamisljeni_broj:
            brojac += 1
            print("Broj je veći od unešenog.")
            print(brojac, ". pokušaj", sep = "")
        elif int(unos_broja) == zamisljeni_broj:
            brojac += 1
            if brojac < 9:
                print(f"Bravo! Pogodili ste broj unatar {brojac} pokušaja.")
                print()
            if brojac > 9:
                print(f"Pogodili ste broj i {brojac} pokušaja.")
                print()
            while True:
                game = str(input("Želite li igrati ponovo? Y/N: ")).lower()
                if game=="y":
                    brojac = 0
                    break
                elif game == "n":
                    igra = 0
                    break
                else:
                    print("krivi unos")
    else:
        print("Niste unjeli broj.")



"""
    broj == zamisljeni_broj:
        print("Pogodak! :)")
    elif broj > zamisljeni_broj:
        print("Broj je manji, pokušajte ponovo.")
    elif broj < zamisljeni_broj:
        print("Broj je veći, pokušajte ponovo.")
    elif 
"""    