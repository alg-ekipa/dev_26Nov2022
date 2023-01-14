'''
Napsati program koji od korisnika ocekuje upis:
2 cijela broja.
Program treba provjeriti i ispisati:
- je li zbroj unesenih brojeva paran ili nije

'''

broj1=int(input("Unesi prvi cijeli broj:"))
broj2=int(input("Unesi drugi cijeli broj:"))

if (broj1+broj2)%2==0:
    print(f"zbroj brojeva {broj1} i {broj2} je paran.")
else:
    print(f"zbroj brojeva {broj1} i {broj2} je nije paran.")

