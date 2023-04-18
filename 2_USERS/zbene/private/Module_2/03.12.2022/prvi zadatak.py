#Napisati python program koji od korisnika očekuje upis 2 broja. Izračunati i ispisati je li zbroj brojeva veći, manji ili jednak 10?

broj_1 = int(input("Upišite prvi od dva broja: "))
broj_2 = int(input("Upišite drugi od dva broja: "))

if broj_1+broj_2 > 10:
    print("Broj je veći od 10")
elif broj_1+broj_2 == 10:
    print("Broj je jednak 10")
else:
    print("Broj je manji od 10")