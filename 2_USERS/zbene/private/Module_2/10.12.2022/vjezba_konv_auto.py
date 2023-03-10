#Ako automobil troši 5.2 litara na 100km i ako je cijena goriva 9.56 kn po litri (nije važno kojeg goriva), izračunajte koliko košta 1km vožnje automobilom. Prikažite mjesečni trošak (30 dana) odlaska na posao automobilom koji je udaljen 20km u jendom smjeru.

automobil = float(input('Unesi potrošnju automobila na 100km: '))
cijena = float(input('Unesi cijenu goriva po litri: '))
mjesec = int(input('Unesi broj dana u mjesecu: '))
put = int(input('Unesi broj putovanja u danu: '))

po_kilometru = automobil*cijena/100
mjesečni_povratni_put = po_kilometru*30*2
print(po_kilometru, 'košta vožnja po kilometru')
print('Mjesečni trošak iznosi', mjesečni_povratni_put, 'kn')