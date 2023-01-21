
ocjene_ucenika=[]
broj_ucenika=input('unesi broj učenika u rezredu:')
broj_ucenika=int(broj_ucenika)+1
for i in range (1,broj_ucenika):
    ocjena=input("'unesi ocjenu ucenika ', i, ':'")
    ocjena=int(ocjena)
    ocjene_ucenika.append(ocjena)
print(ocjene_ucenika)

prosjek_ocjena=0
for ocjena in ocjene_ucenika:
    prosjek_ocjena=prosjek_ocjena+ocjena
print('Ukupno ocjena', prosjek_ocjena)


prosjek_ocjena=prosjek_ocjena/broj_ucenika
print('Broj učenika u razredu je ', broj_ucenika)
print('Prosjek ocjena ovih učenika iznosi', end='')
print(round(prosjek_ocjena,3))

#print('broj petica:', ocjene_ucenika.count(5))