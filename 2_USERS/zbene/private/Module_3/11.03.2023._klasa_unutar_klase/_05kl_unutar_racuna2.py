from _04kl_unutar_racuna import Račun

# Unos više računa

lista_objekata_racuna = []
broj = 1
datum = '1.1.2001.'


while True:
    r = Racun(broj, datum, '', 1)
    lista_stavki = r.unesi_stavke()
    ukupna_cijena = 0
    print(r.broj, r.datum)
    print('--------------------------------------')
    broj+=1
    for stavka in lista_stavki:
        r = Racun(broj, datum, stavka.proizvod, stavka.cijena)
        ukupna_cijena += r.stavka.cijena
        r.ispisi()
    print('__________________________________________')
    print(ukupna_cijena)

    

    pitanje = input('Novi račun?  da / ne   ')
    if pitanje == 'ne':
        break