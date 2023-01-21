#Palindrom

rijec = input("Unesi rijec: ")

obrnuta_rijec = rijec[::-1]

if obrnuta_rijec == rijec:
    print("Rijec je palindrom.")
else:
    print("Rijec nije palindrom.")


