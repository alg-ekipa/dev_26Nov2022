#Ako automobil troši 5.2 litara na 100km i ako je cijena goriva 9.56 kn po litri (nije važno kojeg goriva), izračunajte koliko košta 1km vožnje automobilom. Prikažite mjesečni trošak (30 dana) odlaska na posao automobilom koji je udaljen 20km u jendom smjeru.

automobil = 5.2
cijena = 9.56
mjesec = 30
put = 20

po_kilometru = automobil*cijena/100
mjesečni_povratni_put = po_kilometru*30*2
print(po_kilometru, 'košta vožnja po kilometru')
print('Mjesečni trošak iznosi', mjesečni_povratni_put, 'kn')