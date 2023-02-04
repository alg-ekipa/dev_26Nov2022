# računanje potrošnje goriva ako je mjesečna potrošnja u eurima zadana korisnički

def potrosnja_goriva():
    cijena_goriva=1.40
    km_1=prosjek/100
    km_1_novac=km_1*cijena_goriva
    km_maks=novac/km_1_novac
    return km_maks

prosjek=float(input('Unesite prosječnu potrošnju goriva vašeg automobila na 100km:'))
novac=float(input('Unesite maksimalan iznosu u eurima koji možete potrošiti u 1 mjesecu: '))
print(f'Za {novac} eura možete napraviti maksimalno {round(potrosnja_goriva(),2)} km.')
