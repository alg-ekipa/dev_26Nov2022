class Dogadaj:

    def __init__(self,datum, vrijeme, opis):
        
        self.datum = datum
        self.vrijeme = vrijeme
        self.opis = opis


planer_it = {
    '01.01.23' : [('07:17', 'Test 0101230 7:17'), ('22:17', 'Test 0101230 22:17')],
    '17.04.23' : [('08:17', 'Test 17.04.23 8:17'), ('23:17', 'Test 17.04.23 23:17')],
    '16.11.23' : [('10:17', 'Test 16.11.23 10:17 '), ('21:17', 'Test 16.11.23 21:17')]
   }


print(planer_it)  # TEST, izbrisati kasnije


trazeno_vrijem ='22:17'
trazeni_datum = '01.01.23'


#ispis opisa po traženom vremenu i datumu
               #(trazeni datum, trazeno vrijeme)
def ispis_opisa_datum_vrijeme(trazeni_datum,trazeno_vrijem):
    if trazeni_datum in planer_it.keys():                       #pretražuje postoji li zapis datuma
        lista_dana =list(planer_it[trazeni_datum])              #pretvara vrijednosti u listu
    for x, y in lista_dana:                                     #pretrazuje, postoji li zapis vvremena
        if x == trazeno_vrijem:                                 #x je vrijeme, y je opis u tuplesima
            return y

print(ispis_opisa_datum_vrijeme(trazeni_datum,trazeno_vrijem))
'''

unesni_datum = input('Upišite datum termina: dd.mm.gggg')
if unesni_datum in planer_it.keys(): 
    uneseno_vrijeme = input('Upišite vrijeme termina: hh:mm')
    unesen_opis = input(f'Upišite opis termina u {uneseno_vrijeme}: ')
    planer_it[unesni_datum].append((uneseno_vrijeme,unesen_opis))

print(planer_it)

'''

import os, sys
test_planer = 'im'

# proba da se napravi novi rijecnik, ako ne postoji
try:
    if unesni_datum in planer_im.keys():
        print('Planer postoji')
except NameError:
    print('Still working')
    novi_planer = {}
    print(novi_planer)
    
   # novi_planer = 'planer_' + test_planer




    



# renaming directory ''tutorialsdir"
os.rename(f'{novi_planer}','planer_ {test_planer}')