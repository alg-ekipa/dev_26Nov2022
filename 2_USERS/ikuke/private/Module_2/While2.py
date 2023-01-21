"""
while True:
    print("Sada smo u potencijalno beskonačnoj petlji.")

    odgovor = int(input("Želite li prekinuti petlju? 1 - DA, 0- NE "))

    if odgovor == 1:
        print("Petlja je prekunita.")
        break
    else:
        pass
"""

niz = "Python programer"
for slovo in niz:
    if slovo == "g":
        break
    print(slovo, end = " ")
print()

for slovo in niz:
    if slovo == "g":
        continue
    print(slovo, end = " ")
print()