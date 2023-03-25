import datetime as dt
from planer_klase import Korisnik

lista_korisnik_objekt=[]

upit=input('Želite li dodati korisnika? da/ne? ')
while upit == 'da':
    ime = input('Unesite ime: ')
    prezime =input('Unesite prezime: ')
    god_rod=input('Unesite godinu rođenja: ')
    korisnik_objekt=Korisnik(ime, prezime, god_rod, '', '')
    lista_korisnik_objekt=korisnik_objekt.unesi_termine()
    print(f'{korisnik_objekt.ime} {korisnik_objekt.prezime}, rođen(a) {korisnik_objekt.god_rod} godine ima rezevirani termin: ')
    for korisnik in lista_korisnik_objekt:
        k=Korisnik(ime, prezime, god_rod, korisnik.datum, korisnik.vrijeme)
        k.ispisi_korisnik()
    print()

    upit=input('Želite li dodati korisnika? da/ne? ')
    if upit=='ne':
        break


    
