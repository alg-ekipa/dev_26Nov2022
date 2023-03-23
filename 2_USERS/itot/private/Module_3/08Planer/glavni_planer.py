class Dogadaj:

    def __init__(self,datum, vrijeme, opis):
        
        self.datum = datum
        self.vrijeme = vrijeme
        self.opis = opis


planer_it = {
    '010123' : [('07:17', 'Test 0101230 7:17'), ('22:17', 'Test 0101230 22:17')],
    '170423' : [],
    '161123' : [],
   }


print(planer_it)


trazeno_vrijem ='22:17'
trazeni_datum = '010123'


#ispis opisa po traženom vremenu i datumu
               #(trazeni datum, trazeno vrijeme)
def ispis_opisa_datum_vrijeme(trazeni_datum,trazeno_vrijem):
    if trazeni_datum in planer_it.keys():                       #pretražuje postoji li zapis datuma
        lista_dana =list(planer_it[trazeni_datum])              #pretvara vrijednosti u listu
    for x, y in lista_dana:                                     #pretrazuje, postoji li zapis vvremena
        if x == trazeno_vrijem:                                 #x je vrijeme, y je opis u tuplesima
            return y

print(ispis_opisa_datum_vrijeme(trazeni_datum,trazeno_vrijem))

