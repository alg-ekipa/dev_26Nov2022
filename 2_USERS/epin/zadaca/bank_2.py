import random                                       # POTREBAN ZBOG GENERIRANJA RAČUNA

korisnici = {}                                      # DICT U KOJEM SE POHRANJUJU KORISNICI

def izbornik():                                     # PRVI IZBORNIK
    print('1. Login as admin')
    print('2.Login as korisnik')
    print('3. Izlaz')



##############################  ADMIN FUNKICJE ########################################
# ADMIN 2. FUNKCIJA:
def o_racun():                                              # DODATNA FUNKCIJA ZA GENERIRANJE BROJA RAČUNA
    banka ='123456789'
    racun = ''.join(random.choice('0123456789') for i in range(8))
    return banka + '-'+ racun

def dodaj_korisnika():
    
    ime = input(f'Unesi ime: ')
    prezime = input(f'Unesi prezime: ')
    korisnicko_ime = ime.lower() + prezime[0].lower()
    if korisnicko_ime in korisnici:
        print(f'Korisnik s imenom {korisnicko_ime} već postoji u bazi!')
        return
    lozinka = input(f'Unesi lozinku: ')
    racun = str(o_racun())
    korisnici[korisnicko_ime] = {'ime': ime, 'prezime': prezime, 'lozinka': lozinka, 'o_racun': racun,'stanje': 0}
    print(f'Dodan korisnik: {ime} {prezime} s korisnickim imenom: {korisnicko_ime} i brojem racuna: {racun}')
    input('Pritisnite ENTER za povratak na izbornik...')

# ADMIN 3. FUNKCIJA: 
        #NALAZI SE UNUTAR DEF ADMIN():


# ADMIN 4. FUNKCIJA: 
def dodaj_novac():                                                             
    korisnicko_ime = input('Unesi korisnicko ime: ')
    ime = input(f'Unesi ime: ')
    prezime = input(f'Unesi prezime: ')
    lozinka = input(f'Unesi lozinku: ')
    racun = o_racun()
    balance = float(input('Unesi iznos za uplatu na račun: '))
    korisnici[korisnicko_ime] = {'ime': ime, 'prezime': prezime, 'lozinka': lozinka, 'racun': racun, 'stanje': balance}
    print(f'Dodan korisnik {ime} {prezime} s korisnickim imenom {korisnicko_ime} i brojem racuna {racun} te početnim stanjem računa {balance}')


# ADMIN 5. FUNKCIJA: 

def podigni_novac(korisnici):
    korisnik_ime = input('Unesite svoje korisnicko ime: ')
    if korisnik_ime in korisnici:
        lozinka = input('Unesite lozinku: ')
        if lozinka == korisnici[korisnik_ime]['lozinka']:
            iznos_input = input('Unesite iznos: ')
            try:
                iznos = float(iznos_input)
            except ValueError:
                print("Unesite valjani iznos.")
                return
            if korisnici[korisnik_ime]['stanje'] >= iznos:
                korisnici[korisnik_ime]['stanje'] -= iznos
                print('Uspjesno podignut iznos od', iznos, 'kn.')
                print('Trenutno stanje racuna:', korisnici[korisnik_ime]['stanje'], 'kn.')
            else:
                print('Na racunu nemate dovoljno sredstava za podizanje zadanog iznosa.')
        else:
            print('Pogresna lozinka.')
    else:
        print('Korisnik s tim korisnickim imenom ne postoji.')
    

def admin():                                                                            # LOG KAO ADMIN
        global korisnici                                                                 
        admin_name = input('Unesite ime admina: ')
        admin_password = input('Unesite lozinku admina: ')

        if admin_name == 'admin' and admin_password == 'bank':
            print('Uspješna prijava kao admin.')
            while True:
                print('1. Korisnici')
                print('2. Otvaranje računa')
                print('3. Zatvarnje računa')
                print('4. Dodavanje novaca')
                print('5. Podizanje novaca')
                print('6. Povratak u glavni izbornik')
                
                ad_odabir = input('Odaberite radnju: ')
                
                if ad_odabir == '1':                # ISPISUJE NAM DICT U KOJEM SU UPISANI KLIJENTI
                    print(korisnici)                
                    print
                elif ad_odabir == '2':
                    print('Otvaranje računa: ')
                    dodaj_korisnika()
                    print
                elif ad_odabir == '3':
                    print('Zatvaranje računa: ')
                    korisnik_ime = input('Unesi korisnicko ime: ') 
                    if korisnik_ime in korisnici:
                         admin_password = input('Unesi admin pass: ')
                         if admin_password == 'bank':
                            del korisnici[korisnik_ime]
                            print(f'Korisnik {korisnik_ime} je obrisan.')
                    else:
                        print(f'Korisnik {korisnik_ime} ne postoji u bazi.')
                        print
                elif ad_odabir == '4':
                    print('Dodaj novac')
                    dodaj_novac()
                elif ad_odabir == '5':
                    print('Podigni novac')
                    podigni_novac(korisnici)
                elif ad_odabir == '6':
                    break
                    
                else:
                    print('Pogrešan unos')
        else:
            print('Pogrešno ime ili lozinka admina.')


#################################   KORISNIK FUNKCIJE  ############################################

def korisnik():
    global korisnici
    korisnik_ime = input('Unesite svoje korisnicko ime: ')
    if korisnik_ime in korisnici:
        lozinka = input('Unesite lozinku: ')
        if lozinka == korisnici[korisnik_ime]['lozinka']:
            print('Uspješna prijava kao korisnik.')
            while True:
                print('1. Stanje računa')
                print('2. Dodavanje novaca')
                print('3. Podizanje novaca')
                print('4. Povratak u glavni izbornik')
                odabir = input('Odaberite radnju: ')
                korisnik = korisnici[korisnik_ime]
                if odabir == '1':
                    print(f'Stanje računa korisnika {korisnik["ime"]} {korisnik["prezime"]} {korisnik["racun"]} je: {korisnik["stanje"]}')
                elif odabir == '2':
                    novac = float(input('Unesite iznos novca za dodavanje: '))
                    korisnik["stanje"] += novac
                    print(f'Uspješno ste dodali {novac} kn na račun. Novo stanje računa je: {korisnik["stanje"]}')
                elif odabir == '3':
                    novac = float(input('Unesite iznos novca za podizanje: '))
                    if novac <= korisnik["stanje"]:
                        korisnik["stanje"] -= novac
                        print(f'Uspješno ste podigli {novac} kn sa računa. Novo stanje računa je: {korisnik["stanje"]}')
                    else:
                        print('Nemate dovoljno novca na računu.')
                elif odabir == '4':
                    break
                else:
                    print('Krivi odabir.')
            input('Pritisnite ENTER za povratak na izbornik...')
        else:
            print('Pogrešna lozinka!')
    else:
        print('Korisnik ne postoji!')

                                        
                                        
                   
            

menu = True
while menu == True:
    izbornik()
    odabir = input('Login as: ')

    if odabir == '1':
        admin()
    elif odabir == '2':
        korisnik()
    elif odabir == '3':
        exit()
    else:
        print('Neispravan unos, molimo unesite jedan od ponuđenih odabira (1-3).')
        izbornik()