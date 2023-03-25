import datetime as dt
sada=dt.datetime.now()

class Korisnik:
    def __init__(self, ime, prezime, god_rod, datum, vrijeme):
        self.ime = ime
        self.prezime = prezime
        self.god_rod = god_rod
        self.termin= self.Termin(datum, vrijeme)
    
    def ispisi_korisnik(self):
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
                    print()
                if unos=='ne':
                    break
            return lista_termina_korisnika
    
    class Termin:
        def __init__(self, datum, vrijeme):
            self.datum = datum
            self.vrijeme = vrijeme

        def ispisi_termin(self):
            print(f'Datum: {self.datum}\t vrijeme: {self.vrijeme};')
   