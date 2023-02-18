potrosnja_automobila = 5.3 #l na 100km 
cijena_goriva = 9.56 #po litri
#izračunaj trosak 1 km vožnje, prikaži mjesečni trošak (30 dana) odlaska na posao 20 km u 1 smjeru

trosak_po_km = potrosnja_automobila / 100 * cijena_goriva
print('Potrošnja automobila po kilometru iznosi: ', trosak_po_km, 'kn')

mjesecni_trosak = trosak_po_km * 40 * 30
print('Mjesečni trošak automobila iznosi: ', mjesecni_trosak, 'kn')
