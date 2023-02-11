
broj_kartice = input("Unesite broj kartice:  \n")  # TODO uvjeti i provjera 16 brojeva
kolicina_brojeva = len(broj_kartice)
znak_skrivanja= input('Unesite znak kojim skrivate znamenke (*/#): ') # TODO uvjeti i provjera */#

lista_broj_kartice = list(broj_kartice.strip(" "))
print(lista_broj_kartice)

len_liste = len(lista_broj_kartice)

for slovo in lista_broj_kartice:
    #print(slovo)
    if [slovo] == '-':
        print(slovo,end="")
    else:
        print(znak_skrivanja,end="")
        
##### ne radi, doma rijesiti



'''i=0
while i < kolicina_brojeva - 4:
    while print(znak_skrivanja,end="")
    i+=1
print(broj_kartice[-4:])




print(broj_kartice)
print(kolicina_brojeva)
'''