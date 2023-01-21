import random

zamisljeni_broj = random.randint(1,100)
print(zamisljeni_broj)
brojac=0
igra=1

while True:
    broj = str(input("Unesite broj: "))
    while broj.isdigit==False:
        print("Krivi unos! Morate unijeti BROJ! Ponovite unos!")
        brojac+=1
        print(brojac, "pokusaj", sep=" ")
        broj= input()
    if int(broj) == zamisljeni_broj:
        brojac+=1
        print("Pogodak")
        print(brojac, "pokusaj", sep=" ")
        break
    elif int(broj)== 0:
        break
    elif int(broj) < zamisljeni_broj:
        print("Broj je veci od zadanog")
        brojac+=1
        print(brojac, "pokusaj", sep=" ")
    elif int(broj) > zamisljeni_broj:
        print("Broj je manji od zadanog")
        brojac+=1
        print(brojac, "pokusaj", sep=" ")
while True:
        igra=str(input("želite li igrati ponovno? Y/N ")).lower()
        if igra=="y":
            zamisljeni_broj = random.randint(1, 100)
            brojac=0
            break
            
        elif igra=="n":
            igra=0
            break
        else:
            print("Krivi unos!")
           