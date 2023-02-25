import random
# Zadatak 
# Predefinirani Administrator sustava, koji može dodati nove korisnike u sustav, ažurirati i brisati postojeće.
# Svaki korisnik ima: ime, prezime, korisničko ime (UserName) i Zaporku (Password)
# Zaporka (Password) mora imati, minimalno 10 znakova
# Korisničko ime (UserName) mora biti jedinstveno
#Uspješna prijava na ekranu ispisuje
#poruku: Dobro došli, {ime} {prezime}



korisnici = {
    'admin': ['Marko','Novosel','1234'],
    'markecn' :['Melita','Novosel','4321'],
}


def tko_je_admin():
    for key in korisnici.keys():
        if key == 'admin':
            print(f'Postovani, imate admin ovlasti, slijedi admin izbornik ')
            izbornik_admin()
        else:
            tko_je_korisnik()

def tko_je_korisnik():
    print(f'Postovani imate korisnicke ovlasti, slijedi izbornik za korisnika')
    izbornik_korisnik()

def logiranje():
    uneseni_user = input('Upiši korisničko ime: ')
    if uneseni_user in korisnici.keys():
        uneseni_password = input('Upiši lozinku: ')
        if uneseni_password == korisnici[uneseni_user][2]:
            print(f'Dobro došao, {korisnici[uneseni_user][0]} {korisnici[uneseni_user][1]} ')

#logiranje(uneseni_user)


def dodavanje():
    for i in range(1):
        kljuc = (input(f'Molim unesite user: {i+1}. novog korinsika '))        
        vrijednost_ime = input(f'Molimo unesite ime {i+1}. novog korisnika: ')
        vrijednost_prezime = input(f'Molimo unesite prezime {i+1}. novog korisnika: ')
        vrijednost_lozinka = input(f'Molimo unesite lozinku {i+1}. novog korisnika: ')
        korisnici[kljuc] = [vrijednost_ime, vrijednost_prezime, vrijednost_lozinka]
        print(f'Zavrsili ste unos novog korisnika, prikaz rjecnika: {korisnici}')


def brisanje():
    clan_brisanje = input(f'Unesite user korisnika kojeg zelite pobrisati: ')
    clan_brisanje = korisnici.pop(clan_brisanje)
    print(korisnici)


def pregled():
    print(f'Trenutno aktivni korisnici u rjecniku {korisnici}')

def odjava():
    print(f'Hvala na koristenju!')



def izbornik_korisnik():
    print('1. Pregled')
    print('2. Odjava')
    izbor_korisnik = int(input('Molim unesite broj 1 do 2 ' ))
    if izbor_korisnik == 1:
        pregled()
        izbornik_korisnik()
    if izbor_korisnik == 2:
        odjava()



def izbornik_glavni():
    print('Dobro dosli u Izbornik')

def izbornik_admin():
    print('1. Dodavanje')
    print('2. Brisanje')
    print('3. Pregled')
    print('4. Odjava')
    izbor_admina = int(input('Molim odaberite broj 1 do 4 '))
    if izbor_admina == 1:  
        dodavanje()        
        izbornik_admin()
    elif izbor_admina == 2:
        brisanje()
        izbornik_admin()
    elif izbor_admina == 3:
        pregled()
        izbornik_admin()
    elif izbor_admina == 4:
        odjava()




###############################################

while 1: 
    print('Unesite podatke')    
    logiranje()
    print('_'*100)
    tko_je_admin()
    print('_'*100)
    izbornik_admin()
