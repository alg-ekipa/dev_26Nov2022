

ocjene_ucenika= [3, 2, 4, 4, 3, 5, 5, 2, 1, 3 ]
print(len(ocjene_ucenika))
broj_ocjena=len(ocjene_ucenika)
prosjek=0
for ocjena in ocjene_ucenika: # za svaki broj unutar liste brojevi
    print(ocjena)
    prosjek=prosjek+ocjena
prosjek=prosjek/broj_ocjena
print("prosjek ocjena je", prosjek)

