import os
class bcolors:
    ZELENO = '\033[92m'
    ZUTO = '\033[93m'
    CRVENO = '\033[91m'
    KRAJ = '\033[0m'


trenutni_korisnik='nitko'


vrsta_korisnika = ['admin','referent','klijent']

    #'user_name': ['naziv tvrtke', 'adresa', 'Lozinka', godište osnivanja, vrsta korisnika]
klijenti = {
    'admin': ['BANKA', 'Zagreb', '123456', 2023, 'admin'],
    'referent': ['BANKA', 'zagreb', 'referent1', 1973, 'referent'],
    'igokuk' : ['Igor', 'Zagreb', '123456', 1981,'klijent'],
    'algebra' : ['Algebra', 'Zagreb', 'abc123', 1923, 'klijent'],
    'tecaj' : ['Python', 'WEB', 'filip123', 1998, 'klijent']
}


  #'user_name': [prometi po računima]
racuni_klijenata = {
    'admin': [0.0, 10, -10, 20, -10],
    'referent': [0.0, 20, -10, 20, -10],
    'igokuk' : [0.0, 30, -10, 25, -15],
    'algebra' : [0.0, 40, -10, 20, -10],
    'tecaj' : [0.0, 50, -40, 30, -20]
}

klijenti_izbrisani = {
    'administrator': ['BANKA', 'Zagreb', 'admin1', 2023, 'admin']
}

racuni_klijenata_izbrisani = {
    'administrator': [0.0, 20, -10, 20, -10]
}


korisnici = {
    'admin': ['BANKA', 'Zagreb', '123456', 2023, 'admin'],
    'referent': ['BANKA', 'zagreb', 'referent1', 1973, 'referent'],
    'igokuk' : ['Igor', 'Zagreb', '123456', 1981,'klijent'],
    'algebra' : ['Algebra', 'Zagreb', 'abc123', 1923, 'klijent'],
    'tecaj' : ['Python', 'WEB', 'filip123', 1998, 'klijent']
}


def pregled_korisnici_radno():
    """ Funkcija koja ispisuje sve korisnike iz baza/rječnika """

    for v in korisnici.values():
        #'user_name': ['naziv tvrtke', 'adresa', 'Lozinka', godište osnivanja, vrsta korisnika]
        print(korisnici.keys())
        print(f' Naziv tvrtke: {v[0]}, adresa: {v[1]}, godište osnivanja: {v[3]}, vrsta korisnika: {v[4]}')
    input()




def pregled_korisnici():
    """ Funkcija koja ispisuje sve korisnike iz baza/rječnika """

    for k in klijenti.keys():
                        print()
                        privremena_lista = list(klijenti[k])
                        print (k)

                        for v in privremena_lista:
                            print(f'       {v} ',  end = ' ')
 
    input()



def pregled_korisnici_racuni():

    """ Funkcija koja ispisuje sve račune korisnike iz baza/rječnika """
    pregled_korisnici()

    zeljeni_korisnik=input ('upiši za kojeg korisnika želite ispis prometa: ')
   
   
    for k in racuni_klijenata.keys():
        if (k == zeljeni_korisnik):
            privremena_lista = list(racuni_klijenata[zeljeni_korisnik])

            stanje=0.0
            i=1

            for v in privremena_lista:
                print(f' promet {i} -->{v} EUR')
                stanje = stanje + float(v)
                print(stanje)
                i=i+1
            print(f'stanje računa korisnika {zeljeni_korisnik} je {stanje} EUR')
 
    input()





def tko_je_admin():
    """ Funkcija koja ispisuje ime i prezime administratora """
    for k,v in korisnici.items():
        if (k== 'admin'):
            print(f' Ime: {v[0]}, Prezime: {v[1]}             je Admin')
    input()



#-------------------------------------------------------------------------------

def racun_uplata_isplata(klijent,iznos):
    try:
        float(iznos)


        privremena_lista = list(racuni_klijenata[klijent])
        print('privremena lista početna')
        for v in privremena_lista:
            print (v)
        input()


        privremena_lista.append(iznos)
        print('privremena lista nakon dodavanja uplate/isplate')
        for v in privremena_lista:
            print (v)
        input()

        racuni_klijenata.update({klijent : privremena_lista})

        privremena_lista = list(racuni_klijenata[klijent])
        print('privremena lista iz riječnika nakon dodavanja privremene liste')
        for v in privremena_lista:
            print (v)
        input()

    except:
        print('molim unesite iznos - pogresan unos s tipkovnice')
        input()

#-------------------------------------------------------------------------------



def dodavanje_novog_korisnika_u_listu():
        #punjenje rječnika iz dvije liste - jedna su ključevi, a druga su vrijednosti

    rjecnik_iz_liste = {}

    lista_kljuceva = [1, 2, 3, 4, 5]
    lista_vrijednosti = ['python', 'c++', 'java', 'perl', 'asp.net']

    for i in range (len(lista_kljuceva)):
        kljuc=lista_kljuceva[i]
        vrijednost=lista_vrijednosti[i]
        rjecnik_iz_liste[kljuc]=vrijednost


    for k, v in rjecnik_iz_liste.items():
        print(f'{k} : {v}')
    input()



def dohvati_admin_pswd():
    for k,v in korisnici.items():
        if k== 'admin':
            return v[2]
    input()



def dodavanje_korisnika():
    odg = input ('Želite li se dodati korisnika? da/ne ')
    #'user_name': ['naziv tvrtke', 'adresa', 'Lozinka', godište osnivanja, vrsta korisnika]

#'admin': ['BANKA', 'Zagreb', '123456', 2023, 'admin'],

    if odg == 'da':
        vrsta_korisnika=input('Unesi vrstu korisnika:')
        username_korisnika=input('Unesi korisničko ime:')
        sifra_korisnika=input('Unesi šifru korisnika:')
        naziv_tvrtke=input('Unesi naziv tvrtke:')
        adresa_korisnika=input('Unesi adresu korisnika:')
        godina_osnivanja_korisnika=input('Unesi godinu osnivanja:')
        
        print(f'korisnik razine {vrsta_korisnika} {naziv_tvrtke}, {adresa_korisnika} ima username {username_korisnika} i šifru {sifra_korisnika}')
        korisnici.update({username_korisnika:[naziv_tvrtke,adresa_korisnika,sifra_korisnika,godina_osnivanja_korisnika,vrsta_korisnika]})
        racuni_klijenata.update({username_korisnika:[0]})
        input()
        
        
    else:
        print('unijeli ste da ne želite dodati novog korinika')
        input()



def logiranje(uneseni_username):
    if uneseni_username in korisnici.keys():
        uneseni_password= input('unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username][2]:
            print('-----------------------------------------------------------------------------------')
            print(f'Dobrodosli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
            
            print('-----------------------------------------------------------------------------------')
            input()
            return uneseni_username
        else:
            print('pogrešna lozinka')
            input()
            return 'nitko'


    else:
        print(f'Nepostojeće korisničko ime')
        input()
        return 'nitko'

#-------------------------------------------------------------*************************************************************************************

def izbornik(trenutni_korisnik):
    os.system('cls')
    if trenutni_korisnik == 'nitko':
        print(bcolors.CRVENO+f'aktivni korisnik: {trenutni_korisnik}'+ bcolors.KRAJ)
    else:
        print(bcolors.ZELENO+f'aktivni korisnik: {trenutni_korisnik}'+ bcolors.KRAJ)
    print(' ')
    print(bcolors.ZUTO+ '--------------------------------------' + bcolors.KRAJ)
    print(bcolors.ZUTO+ '---------------IZBORNIK---------------' + bcolors.KRAJ)
    print(bcolors.ZUTO+ '--------------------------------------' + bcolors.KRAJ)
    print()
    print(bcolors.ZELENO+ 'UNESITE ŽELJENI IZBOR'+ bcolors.KRAJ)
    print()
    print('1-prijava u sustav')
    print('2-odjava iz sustava')
    if trenutni_korisnik=='admin':
        print(bcolors.ZELENO+'3-pregled postojećih korisnika'+ bcolors.KRAJ)
    else:  
        print(bcolors.CRVENO+'3-pregled postojećih korisnika'+ bcolors.KRAJ)
    if trenutni_korisnik=='admin':
        print(bcolors.ZELENO+'4-dodavanje novog korisnika'+ bcolors.KRAJ)
    else:  
        print(bcolors.CRVENO+'4-dodavanje novog korisnika'+ bcolors.KRAJ)

    if trenutni_korisnik=='admin' or trenutni_korisnik=='referent':
        print(bcolors.ZELENO+'5-ispis računa korisnika'+ bcolors.KRAJ)
    else:  
        print(bcolors.CRVENO+'5-ispis računa korisnika'+ bcolors.KRAJ)

    if trenutni_korisnik=='admin' or trenutni_korisnik=='referent':
        print(bcolors.ZELENO+'6-uplata na račun korisnika'+ bcolors.KRAJ)
    else:  
        print(bcolors.CRVENO+'6-uplata na račun korisnika'+ bcolors.KRAJ)

    if trenutni_korisnik != 'nitko':
        print(bcolors.ZELENO+'7-isplata sa računa korisnika'+ bcolors.KRAJ)
    else:  
        print(bcolors.CRVENO+'7-isplata sa računa korisnika'+ bcolors.KRAJ)

    
    print(bcolors.ZUTO+'0-IZLAZ'+ bcolors.KRAJ)
    print()
    try:
        izbor=input(bcolors.ZELENO+ '----->>'+ bcolors.KRAJ)
    except:
        izbor=input(bcolors.ZELENO+ '----->>'+ bcolors.KRAJ) 
    try: 
        izbor=int(izbor)


        if izbor==3:
            if trenutni_korisnik == 'nitko':
                username=input('Unesi korisničko ime:')
                trenutni_korisnik=logiranje(username)
                return trenutni_korisnik
            elif trenutni_korisnik == 'admin':
                pregled_korisnici()
                return trenutni_korisnik
            else:
                input(bcolors.CRVENO+'nemate ovlasti za odabranu radnju'+ bcolors.KRAJ)
                return trenutni_korisnik


        elif izbor==4:
            if trenutni_korisnik == 'nitko':
                username=input('Unesi korisničko ime:')
                trenutni_korisnik=logiranje(username)
                return trenutni_korisnik
            elif trenutni_korisnik == 'admin':
                dodavanje_korisnika()
                return trenutni_korisnik
            else:
                input(bcolors.CRVENO+'nemate ovlasti za odabranu radnju'+ bcolors.KRAJ)
                return trenutni_korisnik



        elif izbor==1:
            username=input('Unesi korisničko ime:')
            trenutni_korisnik=logiranje(username)
            return trenutni_korisnik


        elif izbor==2:
            trenutni_korisnik='nitko'
            return trenutni_korisnik


        elif izbor==5:
            if trenutni_korisnik == 'nitko':
                username=input('Unesi korisničko ime:')
                trenutni_korisnik=logiranje(username)
                return trenutni_korisnik

            elif trenutni_korisnik == 'admin' or trenutni_korisnik=='referent':
                pregled_korisnici_racuni()
                return trenutni_korisnik
            else:
                input(bcolors.CRVENO+'nemate ovlasti za odabranu radnju'+ bcolors.KRAJ)
                return trenutni_korisnik


        elif izbor==6:
            if trenutni_korisnik == 'nitko':
                username=input('Unesi korisničko ime:')
                trenutni_korisnik=logiranje(username)
                return trenutni_korisnik

            elif trenutni_korisnik == 'admin' or trenutni_korisnik=='referent':
                pregled_korisnici()
                korisnik_za_uplatu=input('unesite kojem korisniku želite napraviti uplatu: ')
                iznos=input('unesite iznos koji želite uplatiti na račun u EUR: ')

                racun_uplata_isplata(korisnik_za_uplatu,iznos)
                return trenutni_korisnik
            else:
                input(bcolors.CRVENO+'nemate ovlasti za odabranu radnju'+ bcolors.KRAJ)
                return trenutni_korisnik


        elif izbor==7:
                    if trenutni_korisnik == 'nitko':
                        username=input('Unesi korisničko ime:')
                        trenutni_korisnik=logiranje(username)
                        return trenutni_korisnik

                    elif trenutni_korisnik != 'nitko':
                        pregled_korisnici()

                        print('----------------------ISPLATA---------------------------')
                        korisnik_za_uplatu=input('unesite kojem korisniku želite napraviti uplatu SA SVOG RAČUNA: ')

                        iznos=input('unesite iznos koji želite uplatiti na račun u EUR: ')
                        try:
                            iznos_za_isplatu=-1*float(iznos)
                        except:
                            print('pogresan unos s tipkovnice')
                        racun_uplata_isplata(trenutni_korisnik,iznos_za_isplatu)
                        racun_uplata_isplata(korisnik_za_uplatu,iznos)
                        return trenutni_korisnik
                    else:
                        input(bcolors.CRVENO+'nemate ovlasti za odabranu radnju'+ bcolors.KRAJ)
                        return trenutni_korisnik
        


        elif izbor==0:
            return False
            #break
        else:
        
            print(f'pogrešan unos')
            input()
    except:
        print(f'pogrešan unos')
        input()





while True:
    trenutni_korisnik=izbornik(trenutni_korisnik)
    if False==trenutni_korisnik:
        break
