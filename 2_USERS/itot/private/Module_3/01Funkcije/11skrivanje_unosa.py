


broj_kartice = input("Unesite broj kartice:  \n")  # TODO uvjeti i provjera 16 brojeva
kolicina_brojeva = len(broj_kartice)
znak_skrivanja= input('Unesite znak kojim skrivate znamenke (*/#): ') # TODO uvjeti i provjera */#

i=0
while i < kolicina_brojeva - 4:
    print(znak_skrivanja,end="")
    i+=1
print(broj_kartice[-4:])





print(broj_kartice)
print(kolicina_brojeva)
