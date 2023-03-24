import datetime as dt

class Korisnik:
    def __init__(self, ime, prezime, god_rod, datum, vrijeme):
        self.ime = ime
        self.prezime = prezime
        self.god_rod = god_rod
        self.termin= self.Termin(datum, vrijeme)
    
    def ispisi_korisnik(self):
        print(f'{self.ime} {self.prezime}, rođen(a) {self.god_rod} godine ima rezevirani termin:\n')
        self.termin.ispisi_termin()

    def unesi_termine(self):
            lista_termina_korisnika = []
            unos=input('Želite li rezervirati termin? da/ne? ')
            while unos=='da':
                datum_unos = input('Unesite željeni datum u formatu dd.mm.yyyy: ')
                datum_unos_obj = dt.datetime.strptime(datum_unos, '%d.%m.%Y')
                while datum_unos_obj<sada:                                  #provjera da datum nije prošao
                    datum_unos=input('Uneseni datum je prošao, molim unesite željeni datum u formatu dd.mm.yyyy :')
                    datum_unos_obj = dt.datetime.strptime(datum_unos, '%d.%m.%Y')
                else:
                    datum=datum_unos_obj.strftime('%d.%m.%Y')

                    vrijeme_unos= input('Unesite željeno vrijeme termina u formatu hh:mm ')
                    vrijeme_unos_obj = dt.datetime.strptime(vrijeme_unos,'%H:%M')
                    vrijeme=vrijeme_unos_obj.strftime('%H:%M')
                    
                    termin_objekt = self.Termin (datum, vrijeme)
                    lista_termina_korisnika.append(termin_objekt)
                    unos=input('Želite li rezervirati termin? da/ne? ')
                if upit=='ne':
                    break
            return lista_termina_korisnika
    
    class Termin:
        def __init__(self, datum, vrijeme):
            self.datum = datum
            self.vrijeme = vrijeme

        def ispisi_termin(self):
            print(f'Datum: {self.datum}\t vrijeme: {self.vrijeme};')
    
sada=dt.datetime.now()

lista_korisnik_objekt=[]

upit=input('Želite li dodati korisnika? da/ne? ')
while upit == 'da':
    ime = input('Unesite ime: ')
    prezime =input('Unesite prezime: ')
    god_rod=input('Uneste godinu rođenja: ')
    korisnik_objekt=Korisnik(ime, prezime, god_rod, '', '')
    lista_korisnik_objekt=korisnik_objekt.unesi_termine()
    for korisnik in lista_korisnik_objekt:
        k=Korisnik(ime, prezime, god_rod, korisnik.datum, korisnik.vrijeme)
        k.ispisi_korisnik()

    upit=input('Želite li dodati korisnika? da/ne? ')
    if upit=='ne':
        break


    
