import random

brojac = 0

while True:
    zamisljeni_broj = random.randint(1,100)
    print(zamisljeni_broj)

    while True:
        broj = input("Unesite broj: ")
        if broj.isdigit() == False:
            print("Krivi unos! Morate unijeti BROJ! Ponovite unos!")
            brojac += 1
            print(brojac, "pokusaj", sep=" ")
        elif int(broj) == zamisljeni_broj:
            brojac += 1
            print("Pogodak")
            print(brojac, "pokusaj", sep=" ")
            break
        elif int(broj) < zamisljeni_broj:
            print("Broj je veci od zadanog")
            brojac += 1
            print(brojac, "pokusaj", sep=" ")
        elif int(broj) > zamisljeni_broj:
            print("Broj je manji od zadanog")
            brojac += 1
            print(brojac, "pokusaj", sep=" ")

    igra = input("želite li igrati ponovno? Y/N ").lower()
    if igra == "n":
        print("Igra je završena!")
        break
    elif igra != "y":
        print("Krivi unos!")
