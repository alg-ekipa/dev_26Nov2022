from kl_unutar_racuna import Racun

#Unos više računa

lista_objekata_racuna=[]
broj=1
datum='1.1.2001.'
ukupna_cijena=0

while True:
    r=Racun(1,'1.1.2001.', '',1)
    lista_stavki=r.unesi_stavke()
    print(r.broj, r.datum)

    broj+=1
    for stavka in lista_stavki:
        r=Racun(broj, datum, stavka.proizvod, stavka.cijena)
        ukupna_cijena += r.stavka.cijena
        r.ispisi()
    print('_________________________')
    print(ukupna_cijena)

    pitanje=input('Novi račun? da/ne   ')
    if pitanje=='ne':
        break
