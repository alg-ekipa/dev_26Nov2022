from _22_klase_unutar_račun import Račun

# Unos više računa

lista_objekata_računa = []
broj = 1
datum = '1.1.2020.'
ukupna_cijena = 0

while True:
    r = Račun(1, '1.1.2018.', '',1)
    lista_stavki  = r.unesi_stavke()
    print(r.broj, r.datum)

    broj += 1
    for stavka in lista_stavki:
        r = Račun(broj, datum, stavka.proizvod, stavka.cijena)
        ukupna_cijena =+ r.stavka.cijena
        r.ispisi()
        print(ukupna_cijena)
    print('----------------------')

    pitanje = input('Novi račun? da / ne')
    if pitanje == 'ne':
        break