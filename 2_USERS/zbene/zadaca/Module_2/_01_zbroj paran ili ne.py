#Napisati python program koji od korisnika oƒçekuje upis 2 cijela broja. Program treba provjeriti i ispisati je li zbroj unesenih brojeva paran ili nije?

broj_1 = int(input("Upiši prvi od dva broja: "))
broj_2 = int(input("Upiši drugi od dva broja: "))

zbroj = broj_1+broj_2

if zbroj %2 == 0:
    print("Zbroj brojeva iznosi:", zbroj)
    print("Zbroj unešenih brojeva je paran")
else:
    print("Zbroj brojeva iznosi:", zbroj)
    print("Zbroj unešenih brojeva je neparan")