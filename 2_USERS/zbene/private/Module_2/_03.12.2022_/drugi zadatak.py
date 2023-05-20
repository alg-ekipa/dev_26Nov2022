#Napisati python program koji od korisnika očekuje upis 2 broja. Izračunati i ispisati je li zbroj unesena dva broja manji od 3, jednak 3, veći od 3 i manji od 5, jednak 5 ili veći od 5?

broj_1 = int(input("Upišite prvi od dva broja: "))
broj_2 = int(input("Upišite drugi od dva broja: "))

if broj_1+broj_2 < 3:
    print("Broj je veći od 3")
elif broj_1+broj_2 == 3:
    print("Broj je jednak 3")
elif broj_1+broj_2 >3 and broj_1+broj_2 <5:
    print("Broj je veći od 3 a manji od 5")
elif broj_1+broj_2 == 5:
    print("Broj je jednak 5")
else:
    print("Broj je veći od 5")