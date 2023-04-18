from kink_racuni import Racun 

#Unos više računa

lista_objekata_racuna = []
broj = 1
datum = '1.1.1111.'
ukupna_cijena = 0

while True: 
    r = Racun(broj, datum', '', 1)
    lista_stavki = r.unesi_stavke()
    print(r.broj, r.datum)

    broj +=1
    for stavka in lista_stavki: 
        r = Racun(broj, datum, stavka.proizvod, stavka.cijena)
        ukupna_cijena += 

#iskopirati zadatak jer si se tu pogubila