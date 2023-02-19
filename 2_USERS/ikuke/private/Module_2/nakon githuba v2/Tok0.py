'''



TODO:
promjena loznike sa duplom provjerom
formatirati ispise na 2 decimale
funkcijama definirati natpise na pocetku prozora


Riješeno:
- Korisnik - moze samo provjeravati stanje na racunu i svoje podatke
- Referent - moze sve osim mjenjanja i brisanja korisnika
- Isplata - moze biti iz sustava ili nekom drugom klijentu, ne moze više nego ima na racunu
- Uplata - po korsinckom imena
- Prikaz stanja računa
- Prikaz prometa po računu - Sva kretanja po racunima se biljeze 
- Izbornik
- Otvaranje računa tvrtke
- Kada dodamo korisnika dodamo i njegovu listu za prikaz prometa

- relogin kroz cijeli app
- Izlaz iz programa (program se nakon svake akcije vrati na početni izbornik u kojem postoji opcija Izlaz)

'''
import os
class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


vrsta_korisnika = ['admin','referent','klijent']

    #'user_name': ['Ime', 'Prezime', 'Lozinka', godište, vrsta korisnika]
klijenti = {
    'admin': ['Ivan', 'Ivic', 'admin123', 1989, 'a'],
    'referent': ['Hrvoje', 'Horvat', 'pult123', 1973, 'r'],
    'eigokuk' : ['Igor', 'Kukec', '123456VS', 1953,'k'],
    'hhanic' : ['Hana', 'Hanic', 'hana123', 1923, 'k'],
    'fmilic' : ['Filip', 'Milic', 'filip123', 2015, 'k']
}

racuni_klijenata = {
    'a': [10, 20, 35.5, 5, 8, 13, 5,8],
    'referent': [8,5,6,4,1,2,5,3,25,],
    'pperic' : [85,25,65,8.5,63,25],
    'hhanic' : [100,25,125,1258.8,10,85],
    'fmilic' : [9,8,56,25,14,12,12.5,25.4]
}

klijenti_izbrisani = {
    'test1' : ['Proba', 'Probic', 'proba123', 1234, 'k']
}
racuni_klijenata_izbrisani = {
    'test1' : []
}

def provjera_upisanog_korisnika(klijent):
    #provjera korisnickog imena u bazi
    
    while klijent not in klijenti.keys():  
        print(bcolors.FAIL+ '\n\tKorisnicko ime ne postoji u bazi.' + bcolors.ENDC)
        klijent = input('\tUpište ispravno korisničko ime: ')
    return klijent    

def provjera_lozinke(uneseno_korisnicko, uneseni_pswd):
       
    while uneseni_pswd != klijenti[uneseno_korisnicko][2]: 
        print(bcolors.FAIL+ '\n\tKrivo ste unijeli lozinku!' + bcolors.ENDC)
        uneseni_pswd  = input('\tUpište ispravnu lozinku: ')
    
def brojanje_tocke(iznos): 
    if iznos.count('.') + iznos.count(',') == 1:
        iznos=iznos.replace(",",".")
    return iznos

def racun_oduzimanje_novaca(klijent,iznos):
    privremena_lista = list(racuni_klijenata[klijent])
    privremena_vrijednost = racuni_klijenata[klijent][-1] - float(iznos)
    privremena_lista.append(privremena_vrijednost)
    racuni_klijenata.update({klijent : privremena_lista})

def racun_pribrajanje_novaca(klijent_destinacija,iznos):
    privremena_lista = list(racuni_klijenata[klijent_destinacija])
    privremena_vrijednost = racuni_klijenata[klijent_destinacija][-1] + float(iznos)
    privremena_lista.append(privremena_vrijednost)
    racuni_klijenata.update({klijent_destinacija : privremena_lista})

def provjera_svote_za_transfer(iznos,klijent):
                #zamjena zareza tockom, ako posotoji
    if iznos.count('.') + iznos.count(',') == 1:
        iznos=iznos.replace(",",".")
    while (iznos.count('.') + iznos.count(',')) > 1 or iznos.replace(".", "" ).replace(",", "" ).isdigit() == False or float(racuni_klijenata[klijent][-1]) < float(iznos):           
        print('Pogrešan unos.')
        #provjera je li upisani broj sastavljen od brojeva
        if iznos.replace(".", "" ).replace(",", "" ).isdigit() == False:
            iznos = input(bcolors.FAIL+ 'Niste upisali broj. Unesite iznos: ' + bcolors.ENDC)
            iznos = brojanje_tocke(iznos)
        #provjera koliko ima zareza ili tocaka
        elif iznos.count('.') + iznos.count(',') > 1:
            iznos = input(bcolors.FAIL+ 'Krivi unos previše tocka i zareza. Samo decimalno mjesto mora biti odvojeno zarezom. Unesite iznos: ' + bcolors.ENDC)
            iznos = brojanje_tocke(iznos)
        #provjera upisanog broja sa trenutnim stanjem na racunu
        elif float(racuni_klijenata[klijent][-1]) < float(iznos):
            iznos = input(bcolors.FAIL+ 'Upisali ste veći iznos od dozvoljenoga za isplatu: ' + bcolors.ENDC)
            iznos = brojanje_tocke(iznos)
    return iznos

def provjera_svote_za_uplatu(iznos):
        while (iznos.count('.') + iznos.count(',')) > 1 or iznos.replace(".", "" ).replace(",", "" ).isdigit() == False:         
            print('Pogrešan unos.')
            #provjera je li upisani broj sastavljen od brojeva
            if iznos.replace(".", "" ).replace(",", "" ).isdigit() == False:
                iznos = input(bcolors.FAIL+ 'Niste upisali broj. Unesite iznos: ' + bcolors.ENDC)
                brojanje_tocke(iznos)
            #provjera koliko ima zareza ili tocaka
            elif iznos.count('.') + iznos.count(',') > 1:
                iznos = input(bcolors.FAIL+ 'Krivi unos previše tocka i zareza. Samo decimalno mjesto mora biti odvojeno zarezom. Unesite iznos: ' + bcolors.ENDC)
                brojanje_tocke(iznos)
        return iznos

def racun_isplata():
    os.system('cls')
    print(f'''
            ----------------------------------
            |       Isplata sa račun:         |
            ----------------------------------   
    ''')
    klijent =input('Sa kojega računa želite isplatit? (korisničko ime): ')
    klijent =provjera_upisanog_korisnika(klijent)
    korisnik_info(klijent)
    opcija = str(input('''Odaberite opciju: 
        1. Isplata gotovine
        2. Uplatiti drugom klijentu
        0. Izlaz
   
        Vaš odgovor:  '''))
            ### provjera je li broj 0 - 2   
    while  opcija.isdigit() == False or int(opcija) not in [0,1,2]:
        opcija = input(bcolors.FAIL+ 'Unos nije dobar, molimo upište broj u rasponu 0 - 2: \n' + bcolors.ENDC)

            # "intput" je naredba, ne može biti i varijbla
    if int(opcija) in [0,1,2]:
        opcija = int(opcija)

        if opcija == 1:
            iznos = input('Unesite zeljeni iznos: ')
            iznos = provjera_svote_za_transfer(iznos,klijent)
            racun_oduzimanje_novaca(klijent,iznos)
            print(f'Novo stanje racuna je {racuni_klijenata[klijent][-1]} €')

        if opcija == 2:
            os.system('cls')
            print(f'''
                    ----------------------------------
                    |       Isplata sa račun:         |
                    ----------------------------------   
            ''')
            korisnik_info(klijent)           
            klijent_destinacija = input('Na koji račun želite prebaciti novac? (korisničko ime): ')
            klijent_destinacija = provjera_upisanog_korisnika(klijent_destinacija)
            korisnik_info(klijent_destinacija)
            
            print(f'Isplata ide na racun korisnika: \n{klijenti[klijent_destinacija][0]} {klijenti[klijent_destinacija][1]}, {klijenti[klijent_destinacija][3]} \n')
            iznos = input('Unesite zeljeni iznos: ')
            iznos = provjera_svote_za_transfer(iznos,klijent)
            racun_oduzimanje_novaca(klijent,iznos)
            print(f'Novo stanje Vašeg racuna je {racuni_klijenata[klijent][-1]} €')
            racun_pribrajanje_novaca(klijent_destinacija,iznos)

        if opcija == 0:
            print('\t\tIzlazak iz isplata!')    

def racun_uplata():
    os.system('cls')
    print(f'''
            ----------------------------------
            |       Uplata na račun:         |
            ----------------------------------   
    ''')

    #provjera klijenta u bazi
    klijent =input('Unesite željeno destinacijsko korisnicko ime: ')
    klijent =provjera_upisanog_korisnika(klijent)
    korisnik_info(klijent)
    iznos = input('Unesite zeljeni iznos: ')
    #zamjena zareza tockom, ako posotoji
    brojanje_tocke(iznos)
    iznos = provjera_svote_za_uplatu(iznos)

    racun_pribrajanje_novaca(klijent,iznos)
    print(f'Novo stanje racuna je {racuni_klijenata[klijent][-1]} €')

def racun_promet(kljuc):  
    os.system('cls')
    print(f'''
            ----------------------------------
            |  Promet po računu korisnika:   |
            ---------------------------------- ''')  
    if klijenti[kljuc][4] in  ['r','a']:
        kljuc =input('\tUnesite željeno korisnicko ime: \n\t\t')
        kljuc =provjera_upisanog_korisnika(kljuc) 
    print(f'''                     {klijenti[kljuc][0]} {klijenti[kljuc][1]}
                        ''')
    privremena_lista = list(racuni_klijenata[kljuc])
    for broj in privremena_lista: 
        print(f'\t\t\t{broj}\t€')

def korisnik_dodavanje_novog():
    os.system('cls')
    print('''
            ----------------------------------
            |   Dodavanje novog korisnika:   |
            ---------------------------------- ''') 
    n_ime= input('Ime: ')
    n_prezime= input('Pezime: ')
    n_godina= input('Godina rođenja: ')
    #provjera upisa, mora biti 4 broja
    while n_godina.isdigit() == False or len(n_godina) != 4:  
        print(bcolors.FAIL+ 'Pogrešan unos.' + bcolors.ENDC)
        n_godina = input('Morate upisati godinu u obliku GGGG: ')
    n_k_ime= input('Korisnicko ime: ')  
    #Provjera da li je vec u bazi korisnicko ime
    while n_k_ime in klijenti.keys():  
        print(bcolors.FAIL+ 'Korisnicko ime postoji u bazi.' + bcolors.ENDC)
        n_k_ime = input('Upište novo korisničko ime: ')
    n_k_lozinka= input('Korisnicku lozinka: ')  #TODO dupli upis lozinke i provjera jednakosti
    #'uss_name': ['Ime', 'Prezime', 'Lozinka', godište, vrsta korisnika]
    klijenti[n_k_ime]= [n_ime,n_prezime,n_k_lozinka,n_godina, 'k']
    racuni_klijenata[n_k_ime] =[0]
    korisnik_info(n_k_ime)

def korisnik_info(kljuc):
    print(f'''
                -------------------------
                |   Podatci o klijentu   |
                -------------------------''')
    print(f'''
    Ime i Prezime:                 Stanje na računu: {racuni_klijenata[kljuc][-1]} €
    {klijenti[kljuc][0]} {klijenti[kljuc][1]} 
    Godina rođenja:
    {klijenti[kljuc][3]} 
    ''')

def korisnik_info_izbornik(kljuc):
    os.system('cls')
    print(f'''
                -------------------------
                |   Podatci o klijentu   |
                -------------------------''')
    if klijenti[kljuc][4] in  ['r','a']:
        kljuc =input('\tUnesite željeno korisnicko ime: \n\t\t')
        kljuc =provjera_upisanog_korisnika(kljuc)  
    print(f'''
    Ime i Prezime:                 Stanje na računu: {racuni_klijenata[kljuc][-1]} €
    {klijenti[kljuc][0]} {klijenti[kljuc][1]} 
    Godina rođenja:
    {klijenti[kljuc][3]} 
    ''')

def izbornik_osnovni(kljuc):
    os.system('cls')
    print(f'''
                ------------------------
                |       Izbornik        |
                ------------------------''')
    if klijenti[kljuc][4] == 'a':
        opcija = (input('''
                Odaberi željenu funkciju: 
                0. Izlaz iz aplikacije
                1. Promjena operatera

                2. Ispis stranice klijenta
                3. Pregled stanja racuna klijenta
                4. Polog novca na račun
                5. Podizanje novca s računa

                6. Dodavanje novog korisnika
                7. Izmjena podataka klijenta
                8. Brisanje klienta
                9. Izbrisani klijenti
                
                    Vaš odabir je: '''))
        while  opcija.isdigit() == False or int(opcija) not in [0,1,2,3,4,5,6,7,8,9]:
            opcija = input(bcolors.FAIL+ 'Unos nije dobar, molimo upište broj u rasponu 0 - 9: \n' + bcolors.ENDC)  
        return opcija 

    if klijenti[kljuc][4] == 'r':
        opcija = (input('''
                Odaberi željenu funkciju: 
                0. Izlaz iz aplikacije
                1. Promjena operatera

                2. Ispis stranice klijenta
                3. Pregled stanja racuna klijenta
                4. Polog novca na račun
                5. Podizanje novca s računa

                6. Dodavanje novog korisnika
                
                    Vaš odabir je: '''))
        while  opcija.isdigit() == False or int(opcija) not in [0,1,2,3,4,5,6]:
            opcija = input(bcolors.FAIL+ 'Unos nije dobar, molimo upište broj u rasponu 0 - 6: \n' + bcolors.ENDC)   
        return opcija                    
        

    if klijenti[kljuc][4] == 'k':
        opcija = (input('''
                Odaberi željenu funkciju: 
                0. Izlaz iz aplikacije
                1. Promjena operatera

                2. Ispis stranice klijenta
                3. Pregled stanja racuna klijenta
                                
                    Vaš odabir je: ''')) 
        while  opcija.isdigit() == False or int(opcija) not in [0,1,2,3]:
            opcija = input(bcolors.FAIL+ 'Unos nije dobar, molimo upište broj u rasponu 0 - 3: \n' + bcolors.ENDC)   
        return opcija  

def izbornik_kraj(operater):
    #NE staviti ovdje brisanje ekrana
    opcija = (input('''
                Odaberi željenu funkciju: 
                0. Izlaz iz aplikacije
                1. Promjena operatera
                2. Glavni izbornik
                
                    Vaš odabir je: '''))
    while  opcija.isdigit() == False or int(opcija) not in [0,1,2]:
        opcija = input(bcolors.FAIL+ 'Unos nije dobar, molimo upište broj u rasponu 0 - 2 \n' + bcolors.ENDC)  

    if opcija == "0":
        return False, None
    if opcija == "1":
        return True, None
    if opcija == "2":
        return True, operater

def korisnik_brisanje():  #TODO interaput ako ne zelim izbrisati korisnika
    os.system('cls')
    print('''
                ------------------------
                |   Brisanje klijenta  |
                ------------------------''')
    klijent = input("\tUnesite korisnika kojeg želite obirasati:\n\t\t")
    klijent = provjera_upisanog_korisnika(klijent)
    #prebacivanje korisnika u izbrisane
    klijenti_izbrisani[klijent] = klijenti[klijent]
    racuni_klijenata_izbrisani[klijent] = racuni_klijenata[klijent]
    #brisanje korisnika
    klijenti.pop(klijent)
    racuni_klijenata.pop(klijent)
    print(f'\t\t{klijenti_izbrisani[klijent][0]} {klijenti_izbrisani[klijent][1]} je izbrisan !')

def ispis_izbrisanih_klijenata():
    os.system('cls')
    print(f''' 
                ------------------------
                |   Izbrisani klijenti |
                ------------------------''')     
    for kljuc,vrijednost in klijenti_izbrisani.items():
        print(f'''\t\t\t{kljuc} 
\t\t{klijenti_izbrisani[kljuc][0]} \t{klijenti_izbrisani[kljuc][1]} \t{klijenti_izbrisani[kljuc][3]}''') 

def izbornik_korisnik_izmjena_podataka(re_klijent):
    os.system('cls')
    print('''
                ------------------------
                |   Izmjena podataka  |
                ------------------------''')
    print("\t\tIzmjena podataka klijenta.\n")
    klijent = re_klijent
    if re_klijent == 'NA':
        klijent = input("\t\tKorisnicko ime klijenta:\n\t\t")
        klijent = provjera_upisanog_korisnika(klijent)
    korisnik_info(klijent)
    opcija = (input('''
            Koji podatak želite izmjeniti: 
            
            0. Ime
            1. Prezime
            2. Lozinku
            3. Godinu rođenja
            4. Vrsta korisnika
            5. Korisničko ime
            6. Izlaz

            Vaš odabir je: '''))
    while  opcija.isdigit() == False or int(opcija) not in [0,1,2,3,4,5,6]:
        opcija = input(bcolors.FAIL+ 'Unos nije dobar, molimo upište broj u rasponu 0 - 6: \n' + bcolors.ENDC)  

    return opcija,klijent

def promjena_imena(klijent):
    os.system('cls')
    print('''
                ------------------------
                |   Izmjena podataka  |
                ------------------------
                   | Izmjena imena |''')    
    novo_ime = input('\n\tUnesite novo ime korisnika:\n\t\t')
    klijenti[klijent][0]= novo_ime
    korisnik_info(klijent)                      #info o klijentu
    return klijent                              #povratak korisnickog imena
 
def promjena_prezimena(klijent): 
    os.system('cls')
    print('''
                ------------------------
                |   Izmjena podataka  |
                ------------------------
                 | Izmjena prezimena |''') 
    novo_prezime = input('\t\tUnesite novo prezime korisnika:\n\t\t')
    klijenti[klijent][1]= novo_prezime
    korisnik_info(klijent)                      #info o klijentu
    return klijent                              #povratak korisnickog imena

def promjena_lozinke(klijent):  #TODO provjera lozinke prije promjene
    os.system('cls')
    print('''
                ------------------------
                |   Izmjena podataka  |
                ------------------------
                 | Izmjena lozinke |''') 
    nova_lozinka = input('\t\tUnesite novo prezime korisnika:\n\t\t')
    klijenti[klijent][2]= nova_lozinka
    korisnik_info(klijent)                      #info o klijentu
    return klijent                              #povratak korisnickog imena

def promjena_godine(klijent):
    os.system('cls')
    print('''
                ------------------------
                |   Izmjena podataka  |
                ------------------------
                   | Izmjena godine |''') 
    novo_godina = input('Godina rođenja: ')
    #provjera upisa, mora biti 4 broja
    while novo_godina.isdigit() == False or len(novo_godina) != 4:  
        print('Pogrešan unos.')
        novo_godina = input(bcolors.FAIL+ 'Morate upisati godinu u obliku GGGG: ' + bcolors.ENDC)  
    klijenti[klijent][3]= novo_godina
    korisnik_info(klijent)                      #info o klijentu
    return klijent                              #povratak korisnickog imena

def promjena_vrsta_korisnika(klijent):  
    os.system('cls')
    print('''
                ------------------------
                |   Izmjena podataka  |
                ------------------------
                   | Izmjena godine |''')  
    nova_vrsta = input('''
        Vrsta korisnika:
            a - administartor
            r - referent
            k - korisnik
            Odaberite vrstu: ''')
    
    while nova_vrsta not in vrsta_korisnika:  
        print('Pogrešan unos.')
        nova_vrsta= input(bcolors.FAIL+ 'Morate upisati a, r ili k: ' + bcolors.ENDC)  
    klijenti[klijent][4]= nova_vrsta
    korisnik_info(klijent)                      #info o klijentu
    return klijent                              #povratak korisnickog imena

def promjena_korisnico_ime(klijent): 
    os.system('cls')
    print('''
                ------------------------
                |   Izmjena podataka  |
                ------------------------
              | Izmjena korisnickog imena |''') 
    novo_korisnicko = input(f'\n\tTreunto korisnicko ime je: \n\t\t{klijent} \n\n\tUnesite novo korisnicko ime:\n\t\t')
    #provjera jel novo ime vec u bazi
    while novo_korisnicko in klijenti.keys():  
        print(bcolors.FAIL+ '\n\tKorisnicko ime postoji u bazi.' + bcolors.ENDC)  
        novo_korisnicko = input('\tUpište novo korisničko ime: \n\t\t')  

    #mjenjanje korisnickog keya / imena u korisnicima
    klijenti[novo_korisnicko] = klijenti[klijent]
    del klijenti[klijent]
    #mjenjanje korisnickog keya / imena u racunima
    racuni_klijenata[novo_korisnicko] =racuni_klijenata[klijent]
    del racuni_klijenata[klijent]
    korisnik_info(novo_korisnicko)                      #info o klijentu
    return novo_korisnicko                             #povratak korisnickog imena

def login():
    print('''
                ------------------------
                |       Log in         |
                ------------------------''')
    uneseno_korisnicko =  input('\t\tKorisnicko ime: ')
    uneseno_korisnicko = provjera_upisanog_korisnika(uneseno_korisnicko)
    if uneseno_korisnicko in klijenti.keys():
        uneseni_pswd = input('\t\tUnesi lozinku: ')
        provjera_lozinke(uneseno_korisnicko, uneseni_pswd)
    return uneseno_korisnicko

aplikacija = True  
while aplikacija == True: 
    os.system('cls')
    operater = login()

    while operater != None:
        odabir = izbornik_osnovni(operater)
        if odabir == "0":
            aplikacija = False 
            operater = None
        if odabir == "1":
            operater = None
        if odabir == "2":
            korisnik_info_izbornik(operater)
            aplikacija, operater = izbornik_kraj(operater)
        if odabir == "3":
            racun_promet(operater) 
            aplikacija, operater = izbornik_kraj(operater)
        if odabir == "4":
            racun_uplata()
            aplikacija, operater = izbornik_kraj(operater)
        if odabir == "5":
            racun_isplata()
            aplikacija, operater = izbornik_kraj(operater)
        if odabir == "6":
            korisnik_dodavanje_novog()
            aplikacija, operater = izbornik_kraj(operater)
        if odabir == "7":
            re_klijent = 'NA'           #resetiranje korisnika za izmjenu
            izbornik_izmjene = True
            while izbornik_izmjene == True:
                podatak,klijent = izbornik_korisnik_izmjena_podataka(re_klijent)    
                if  podatak == "0":
                    re_klijent = promjena_imena(klijent)
                if  podatak == "1":
                    re_klijent = promjena_prezimena(klijent)
                if  podatak == "2":
                    re_klijent = promjena_lozinke(klijent)               
                if  podatak == "3":
                    re_klijent = promjena_godine(klijent)
                if  podatak == "4":
                    re_klijent = promjena_vrsta_korisnika(klijent)
                if  podatak == "5":
                    re_klijent = promjena_korisnico_ime(klijent)
                if  podatak == "6":
                    os.system('cls')
                    izbornik_izmjene = False   #izlazak iz izmjena tog korisnika
            aplikacija, operater = izbornik_kraj(operater)
        if odabir == "8":
            korisnik_brisanje()    
            aplikacija, operater = izbornik_kraj(operater)
        if odabir == "9":
            ispis_izbrisanih_klijenata()
            aplikacija, operater = izbornik_kraj(operater)