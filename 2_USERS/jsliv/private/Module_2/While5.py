#Pogodi broj
import random

zamisljeni_broj = random.randint(1,20)
#print(zamisljeni_broj)

#pogodi = 24


while True:
    broj = int(input("Pogodi broj: "))

    if broj == zamisljeni_broj:
        print("Pogodak! :)")
        break
    elif broj > zamisljeni_broj:
        print("Traženi broj je manji.")
    elif broj < zamisljeni_broj:
        print("Traženi broj je veći.")
