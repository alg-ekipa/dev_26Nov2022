'''
Napravite program za
rad na pultu u banci
Program za sada izvršava u konzoli
Funkcionalnosti:
• Izbornik
• Otvaranje računa tvrtke
• Prikaz stanja računa
• Prikaz prometa po računu
• Polog novca na račun
• Podizanje novca s računa
• Izlaz iz programa (program se nakon
svake akcije vrati na početni izbornik
u kojem postoji opcija Izlaz)

TODO:

• Izlaz iz programa (program se nakon svake akcije vrati na početni izbornik u kojem postoji opcija Izlaz)
promjena loznike sa duplom provjerom

relogin kroz cijeli app
formatirati ispise na 2 decimale
isplata drugom korisniku ili isplata van banke

Riješeno:
• Polog novca na račun
• Podizanje novca s računa
kod dodavanja ili skidanja novaca, zadnji podatak u racun_klijenti i onda + ili -
• Prikaz stanja računa
• Prikaz prometa po računu
• Izbornik
• Prikaz stanja računa
• Prikaz prometa po računu
• Otvaranje računa tvrtke
Kada dodamo korisnika dodamo i njegovu listu za prikaz prometa



'''

    #'uss_name': ['Ime', 'Prezime', 'Lozinka', godište, vrsta korisnika]
klijenti = {
    'admin': ['Ivan', 'Ivic', 'admin123', 1989, 'a'],
    'referent': ['Hrvoje', 'Horvat', 'pult123', 1973, 'r'],
    'pperic' : ['Petar', 'Peric', 'pero123', 1953,'k'],
    'hhanic' : ['Hana', 'Hanic', 'hana123', 1923, 'k'],
    'fmilic' : ['Filip', 'Milic', 'filip123', 2015, 'k']
}

racuni_klijenata = {
    'admin': [10, 20, 35.5, 5, 8, 13, 5,8],
    'referent': [8,5,6,4,1,2,5,3,25,],
    'pperic' : [85,25,65,8.5,63,25],
    'hhanic' : [100,25,125,1258.8,10,85],
    'fmilic' : [9,8,56,25,14,12,12.5,25.4]
}

def ispis_stranice_klijenta(kljuc):
    print(f'''
                -------------------------
                |   Podatci o klijentu   |
                -------------------------
    Ime i Prezime:                 Stanje na računu: {racuni_klijenata[kljuc][-1]} €
    {klijenti[kljuc][0]} {klijenti[kljuc][1]} 
    Godina rođenja:
    {klijenti[kljuc][3]} 
    ''')

def kretanje_po_racunu(kljuc):  
    print(f'''
            ----------------------------------
            |  Kretanje po računu korisnika: |
            ----------------------------------   
                        {klijenti[kljuc][0]} {klijenti[kljuc][1]}
                        ''')
    privremena_lista = list(racuni_klijenata[kljuc])
    for broj in privremena_lista: 
        print(f'\t\t\t{broj}\t€')

def dodavanje_novog_klijenta():
    '''dodavanje novog korisnika'''
    n_ime= input('Ime: ')
    n_prezime= input('Pezime: ')
    n_godina= input('Godina rođenja: ')
    #provjera upisa, mora biti 4 broja
    while n_godina.isdigit() == False or len(n_godina) != 4:  
        print('Pogrešan unos.')
        n_godina = input('Morate upisati godinu u obliku GGGG: ')
    n_k_ime= input('Korisnicko ime: ')  
    #Provjera da li je vec u bazi korisnicko ime
    while n_k_ime in klijenti.keys():  
        print('Korisnicko ime postoji u bazi.')
        n_k_ime = input('Upište novo korisničko ime: ')
    n_k_lozinka= input('Korisnicku lozinka: ')  #TODO dupli upis lozinke i provjera jednakosti
    #'uss_name': ['Ime', 'Prezime', 'Lozinka', godište, vrsta korisnika]
    klijenti[n_k_ime]= [n_ime,n_prezime,n_k_lozinka,n_godina, 'k']
    racuni_klijenata[n_k_ime] =[]


def pologanje_novac():
    print(f'''
            ----------------------------------
            |       Uplata na račun:         |
            ----------------------------------   
    ''')

    #provjera klijenta u bazi
    klijent =input('Unesite željeno destinacijsko korisnicko ime: ')
    while klijent not in klijenti.keys():  
        print('Korisnicko ime ne postoji u bazi.')
        klijent = input('Upište ispravno korisničko ime: ')
    print(f'Uplata ide na racun korisnika {klijenti[klijent][0]} {klijenti[klijent][1]}, {klijenti[klijent][3]} ')
    print(f'Trenutno stanje racuna je {racuni_klijenata[klijent][-1]} €')

    iznos = input('Unesite zeljeni iznos: ')
    #zamjena zareza tockom, ako posotoji
    if iznos.count('.') + iznos.count(',') == 1:
        iznos=iznos.replace(",",".")
    while (iznos.count('.') + iznos.count(',')) > 1 or iznos.replace(".", "" ).replace(",", "" ).isdigit() == False:         
        print('Pogrešan unos.')
        #provjera je li upisani broj sastavljen od brojeva
        if iznos.replace(".", "" ).replace(",", "" ).isdigit() == False:
            iznos = input('Niste upisali broj. Unesite iznos: ')
            if iznos.count('.') + iznos.count(',') == 1:
                 iznos=iznos.replace(",",".")
        #provjera koliko ima zareza ili tocaka
        elif iznos.count('.') + iznos.count(',') > 1:
            iznos = input('Krivi unos previše tocka i zareza. Samo decimalno mjesto mora biti odvojeno zarezom. Unesite iznos: ')
            if iznos.count('.') + iznos.count(',') == 1:
                 iznos=iznos.replace(",",".")

    privremena_lista = list(racuni_klijenata[klijent])
    privremena_vrijednost = racuni_klijenata[klijent][-1] + float(iznos)
    privremena_lista.append(privremena_vrijednost)
    racuni_klijenata.update({klijent : privremena_lista})
    print(f'Novo stanje racuna je {racuni_klijenata[klijent][-1]} €')

def isplata_sa_racuna():
    print(f'''
            ----------------------------------
            |       Isplata sa račun:         |
            ----------------------------------   
    ''')
    #provjera korisnickog imena u bazi
    klijent =input('Sa kojega računa želite isplatit? (korisničko ime): ')
    while klijent not in klijenti.keys():  
        print('Korisnicko ime ne postoji u bazi.')
        klijent = input('Upište ispravno korisničko ime: ')
   
    print(f'Isplata ide na racun korisnika {klijenti[klijent][0]} {klijenti[klijent][1]}, {klijenti[klijent][3]} ')
    print(f'Trenutno stanje racuna je {racuni_klijenata[klijent][-1]} €')

    iznos = input('Unesite zeljeni iznos: ')
    #zamjena zareza tockom, ako posotoji
    if iznos.count('.') + iznos.count(',') == 1:
        iznos=iznos.replace(",",".")
    while (iznos.count('.') + iznos.count(',')) > 1 or iznos.replace(".", "" ).replace(",", "" ).isdigit() == False or float(racuni_klijenata[klijent][-1]) < float(iznos):           
        print('Pogrešan unos.')
        #provjera je li upisani broj sastavljen od brojeva
        if iznos.replace(".", "" ).replace(",", "" ).isdigit() == False:
            iznos = input('Niste upisali broj. Unesite iznos: ')
            if iznos.count('.') + iznos.count(',') == 1:
                 iznos=iznos.replace(",",".")
        #provjera koliko ima zareza ili tocaka
        elif iznos.count('.') + iznos.count(',') > 1:
            iznos = input('Krivi unos previše tocka i zareza. Samo decimalno mjesto mora biti odvojeno zarezom. Unesite iznos: ')
            if iznos.count('.') + iznos.count(',') == 1:
                 iznos=iznos.replace(",",".")
        #provjera upisanog broja sa trenutnim stanjem na racunu
        elif float(racuni_klijenata[klijent][-1]) < float(iznos):
            iznos = input('Upisali ste veći iznos od dozvoljenoga za isplatu: ')
            if iznos.count('.') + iznos.count(',')== 1:
                iznos=iznos.replace(",",".")

    privremena_lista = list(racuni_klijenata[klijent])
    privremena_vrijednost = racuni_klijenata[klijent][-1] - float(iznos)
    privremena_lista.append(privremena_vrijednost)
    racuni_klijenata.update({klijent : privremena_lista})
    print(f'Novo stanje racuna je {racuni_klijenata[klijent][-1]} €')


def izbornik(kljuc):
    print(f'''
                ------------------------
                |       Izbornik        |
                ------------------------''')
    if klijenti[kljuc][4] == 'a':
        option = str(input('''
                Odaberi željenu funkciju: 
                0. Izlaz iz aplikacije
                1. Ispis stranice klijenta
                2. Pregled stanja racuna klijenta
                3. Polog novca na račun
                4. Podizanje novca s računa
                6. Izmjena podataka klijenta
                7. Brisanje klienta
                
                    Vaš odabir je: '''))

    if klijenti[kljuc][4] == 'r':
        option = str(input('''
                Odaberi željenu funkciju: 
                0. Izlaz iz aplikacije
                1. Ispis stranice klijenta
                2. Pregled stanja racuna klijenta
                3. Polog novca na račun
                4. Podizanje novca s računa      
                
                    Vaš odabir je: '''))
    if klijenti[kljuc][4] == 'k':
        option = str(input('''
                Odaberi željenu funkciju: 
                0. Izlaz iz aplikacije
                1. Ispis stranice klijenta
                2. Pregled stanja racuna klijenta
                
                    Vaš odabir je: '''))                

def logiranje():
    ''' logiranje korisnika '''
    uneseno_korisnicko =  input(' Unesi korisnicko ime: ')
    if uneseno_korisnicko in klijenti.keys():
        uneseni_pswd = input('Unesi lozinku:\n')
        if uneseni_pswd == klijenti[uneseno_korisnicko][2]:
            print(f'Dobrodosli,  {klijenti[uneseno_korisnicko][0]} {klijenti[uneseno_korisnicko][1]}')
        else:
            print('Pogresna lozinka')

    else:
        print('Pogresno korisnicko ime!')

     

'''ispis_stranice_klijenta('pperic')
kretanje_po_racunu('pperic')
dodavanje_novog_klijenta()'''
#print(klijenti)
#print(racuni_klijenata)
#izbornik('admin')
#pologanje_novac()
#ispis_stranice_klijenta('pperic')
#kretanje_po_racunu('pperic')
isplata_sa_racuna()