stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }

class Stolovi:
    def __init__(self,naziv, cijena, raspolozivost, dimenzije, boja, materijal):
        self.naziv=naziv
        self.cijena=cijena
        self.raspolozivost=raspolozivost
        self.dimezije=dimenzije
        self.boja=boja
        self.materijal=materijal

    def ispis(self):
        print(f'\n Naziv: {self.naziv}\n Cijena: {self.cijena}\n Raspolozivost: {self.raspolozivost}\n Dimenzije: {self.dimezije}\n Boja: {self.boja}\n Materijal: {self.materijal}')

lista_objekata_stolovi= []

for vrijednost in stolovi_rjecnik.values():
    n = vrijednost[0]
    c = vrijednost[1]
    r = vrijednost[2]
    d = vrijednost[3]
    b = vrijednost[4]
    m = vrijednost[5]
    stolovi_objekt= Stolovi(n,c,r,d,b,m)
    stolovi_objekt.ispis()
    
    lista_objekata_stolovi.append(stolovi_objekt)