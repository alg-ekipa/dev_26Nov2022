class Stolovi:

    def __init__(self,naziv_stola, cijena, raspolozivost, dimenzije, boja, materijal):
        self.naziv_stola = naziv_stola
        self.cijena = cijena
        self.raspolozivost = raspolozivost
        self.dimenzije = dimenzije
        self.boja= boja
        self.materijal= materijal


stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }


lista_stolova = []

for vrijednost in stolovi_rjecnik.values():
    v = vrijednost[0]
    p = vrijednost[1]
    r = vrijednost[2]
    g = vrijednost[3]
    c = vrijednost[4]
    h = vrijednost[5]
    stolovi_objekti = Stolovi(v, p, r, g, c, h)
    lista_stolova.append(stolovi_objekti)

print(lista_stolova)