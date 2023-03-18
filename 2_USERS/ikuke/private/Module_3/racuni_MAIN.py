from racun_klasa_vise_klasa_unutar_klase import Racun

#unos više računa

lista_objekata_racuna = []

broj=1


while True:
    r= Racun (broj, '1.1.2021.', '', 1)
    lista_stavki = r.unesi_stavke()
    print (r.broj, r.datum)


    broj +=1
    for stavka in lista_stavki:
        r= Racun(broj, datum, stavka.proizvod, stavka.cijena)
        ukupna_cijena +=r.stavka.cijena
        r.ispisi()
    print(ukupna_cijena)

    pitanje = input ('Novi racun? da/ne   ')
    if pitanje == 'ne':
        break

