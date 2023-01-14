'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću
vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:
• Ako automobil troši 5.3 litara na 100 km i ako je cijena goriva 9.56 kn
po litri (nije važno kojeg goriva), izračunajte koliko košta 1 km vožnje
automobilom. Prikažite mjesečni trošak (30 dana) odlaska na posao
automobilom koji je udaljen 20 km u jednom smjeru.

'''

potrosnja_auta = 5.3
cijena_goriva = 9.56
dana_u_mjesecu = 30
put_do_posla = 20

cijena_1_km = (potrosnja_auta*cijena_goriva)/100
print (f'Cijena 1 km je {cijena_1_km} kn')

troskovi_do_posla= cijena_1_km*put_do_posla*2*dana_u_mjesecu
print (f'Trosak puta na posao za {dana_u_mjesecu} je {troskovi_do_posla} kn')