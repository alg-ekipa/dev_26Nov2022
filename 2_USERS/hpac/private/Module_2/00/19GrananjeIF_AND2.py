'''
Napisati program kojid od korisnika ocekuje upis 2 broja
Izracunati i ispisati:
- je li zbroj unesena 2 broja manji od 3, jednak 3, veci od 3 manji od 5, jednak 5,  veci od 5
'''


a=int(input("Unesi prvi broj:"))
b=int(input("Unesi drugi broj:"))

if a+b < 3:
    print(" zbroj je manji od 3")
elif a+b == 3:
    print(" zbroj je jednak 3")
elif a+b > 3 and a+b < 5:
    print("zbroj je veci od 3 i manji od 5")
elif a+b == 5:
    print(" zbroj je jednak 5")
elif a+b > 5:
    print(" zbroj je veci od 5")