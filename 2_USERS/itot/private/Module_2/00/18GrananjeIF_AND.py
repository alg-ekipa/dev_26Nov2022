'''
Napisati program kojid od korisnika ocekuje upis 2 broja
Izracunati i ispisati:
- je li zbroj brojeva veci, manji ili jedan 10

'''


a=int(input("Unesi prvi broj:"))
b=int(input("Unesi drugi broj:"))

if a+b > 10:
    print(" zbroj je veci od 10")
elif a+b < 10:
    print(" zbroj je manji od 10")
else:
    print("zbroj je jednak 10")