import os

stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }

   
class Stolovi: 
    def __init__(self, naziv, cijena, raspolozivost, dimenzije, boja, materijal):
        self.naziv = naziv
        self.cijena = cijena
        self.raspolozivost = raspolozivost
        self.dimenzije = dimenzije
        self.boja = boja
        self.materijal = materijal

    def ispis(self):
        print(f'\nNaziv: {self.naziv}\nCijena: {self.cijena}\nRaspolozivost: {self.raspolozivost}\ndimenzije: {self.dimenzije}\nBoja: {self.boja}')

    def ispis_raspolozivost(self):
        if self.raspolozivost == 'True':
            self.ispis()




os.system('cls')


for i in range(6):
    #proizvodac= input ('Unesi proizvodaca automobila:')
    #model = input ('Unesi model automobila:')
    stol=stolovi_rjecnik[i+1]
    stol_objekt= stolovi_rjecnik(vozilo[0],vozilo[1], "bijela", "diesel", vozilo[4])
    lista_objekata.append(auto_objekt)