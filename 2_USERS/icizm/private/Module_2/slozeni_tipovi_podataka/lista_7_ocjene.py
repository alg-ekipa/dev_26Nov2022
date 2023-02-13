#izračunati prosjek ocjena učenika 
ocjene_ucenika = [3, 4, 5, 5, 1, 4, 3, 5, 4, 2]

broj_ocjena = len(ocjene_ucenika) #len govori koliko ocjena imamo u listi (koliko elemenata)

zbroj = 0    #mora biti izvan for

for ocjena in ocjene_ucenika:
    
    zbroj = zbroj + ocjena
prosjek = zbroj / broj_ocjena

print(f'Prosjek ocjena ovog učenika iznosu {prosjek}')

print(sum(ocjene_ucenika))
print(zbroj)
    
