ocjene_ucenika = [3, 2, 4, 4, 3, 5, 5, 2, 1, 3]
broj_ocjena = (len(ocjene_ucenika)) #vidjeti koliko ima ocjena

zbroj = 0
for ocjena in ocjene_ucenika:
    #print(ocjena) samo test
    zbroj = ocjena+zbroj
prosjek = zbroj/broj_ocjena

print(f'Prosječna ocjena iznosi {round(prosjek,2)}') #ime varijable a drugo broj decimala

print(sum(ocjene_ucenika))
print(zbroj)