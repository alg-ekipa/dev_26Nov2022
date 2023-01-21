#PALINDROM

#rijec = input("Unesi rijec: ")

rijec = input("Unesi rijec: ")

o_rijec = rijec[::-1]
#print(o_rijec)

if o_rijec == rijec:
    print("Rijec je palindrom")
else: 
    print("Rijec nije palindrom")