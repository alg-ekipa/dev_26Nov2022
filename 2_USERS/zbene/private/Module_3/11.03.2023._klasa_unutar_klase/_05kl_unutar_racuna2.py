from _04kl_unutar_racuna import Račun

#unos više računa

lista_objekata_računa = []
broj = 1
datum = '01.01.2001.'
ukupna_cijena = 0

while True:
    r = Račun (broj, '01.01.2001.', '', 1)
    lista_stavki = r.unesi_stavke()
    print (r.broj, r.datum)

    broj +=1
    for stavka in lista_stavki:
        r = Račun (broj, datum, stavka.proizvod, stavka.cijena)
        ukupna_cijena += r.stavka.cijena
        r.ispiši()
        print('_______________________')
        print (ukupna_cijena)

    pitanja = input ('Novi račun? da / ne')
    if pitanja == 'ne':
        break