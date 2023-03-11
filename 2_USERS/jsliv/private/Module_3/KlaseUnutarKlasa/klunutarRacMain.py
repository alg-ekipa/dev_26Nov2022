from klasunutklasRacun import Racun


lista_objekata_racuna = []
broj = 1
datum = "3.1.2023."
ukupna_cijena = 0

while True:
    r = Racun(broj, datum, "", 1)
    lista_stavki = r.unos_stavki()
    ukupna_cijena = 0
    print(r.broj, r.datum)
    print("------------------------")
    broj += 1

    for stavka in lista_stavki:
        r = Racun(broj, datum,stavka.proizvod, stavka.cijena)
        ukupna_cijena += r.stavka.cijena
        r.ispisi()
    print(ukupna_cijena)

    pitanje = input("Novi racun DA/NE: ")
    if pitanje == "NE":
        break



