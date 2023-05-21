#Napisati python program koji od korisnika očekuje upis 2 cijela broja. Program treba provjeriti i ispisati je li umnožak unesenih brojeva paran ili nije?

broj_1 = int(input("Upiši prvi od dva broja: "))
broj_2 = int(input("Upiši drugi od dva broja: "))

umnožak = broj_1*broj_2

if umnožak %2 == 0:
    print("Umnožak brojeva iznosi:", umnožak)
    print("Umnožak unešenih brojeva je paran")
else:
    print("Umnožak brojeva iznosi:", umnožak)
    print("Umnožak unešenih brojeva je neparan")