from vozni_park_podaci import vozni_park, Vozilo


lista_objekata_vozila = []

for vrijednost in vozni_park.values():
    v = vrijednost[0]
    p = vrijednost[1]
    r = vrijednost[2]
    g = vrijednost[3]
    c = vrijednost[4]
    vozilo_objekt = Vozilo(v, p, r, g, c)
    #vozilo_objekt.ispis()
    lista_objekata_vozila.append(vozilo_objekt)

#print(lista_objekata_vozila)

# ZADATAK: ispisati sva dostavna vozila - metoda ispis_dostavno() piše se u klasu Vozilo
for vozilo in lista_objekata_vozila:
    vozilo.ispis_dostavna()

#TO DO:
# 1. ispišite sva vozila starija od 2015.
# 2. ispis vozila tražene registracije

trazena_rega = input('Unesite registraciju za pretragu: ')
for vozilo in lista_objekata_vozila:
    vozilo.trazi_regu(trazena_rega)








