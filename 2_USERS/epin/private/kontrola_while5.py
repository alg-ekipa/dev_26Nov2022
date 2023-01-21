#IGRA POGODI BROJ
import random

zamisljeni_broj = random.randint(1,20)
#print(zamisljeni_broj)

while True:
    broj=int(input("Unesite broj: "))
    while broj.isdigit() == True:
        if broj == zamisljeni_broj:
            print("Pogodili ste broj")
            break
        elif broj==0:
            break
        elif broj > zamisljeni_broj:
            print("Broj je veci od zadanog")
        elif broj < zamisljeni_broj:
            print("Broje je manji od zadanog")


#TO DO 
# unos stringa
# raspon brojeva 
#nova igra
