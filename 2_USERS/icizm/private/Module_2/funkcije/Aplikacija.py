import datetime as dt

korisnici = {'korisnik1': {'ime':'Petar', 'prezime':'Petrović', 'lozinka':'1234567', 'stanje': 12345, 'promet':[]}}
#print(korisnici['korisnik1'])

def izbornik():
    odabir = input('Dobar dan! Odaberite jednu od sljedećih opcija: \n\t 1) login \n\t 2) otvaranje računa  ')
    if odabir == '1': 
        uneseni_username = input('Unesite svoje korisničko ime: ')
        logiranje(uneseni_username)
    if odabir == '2': 
        otvaranje_racuna()

def logiranje(uneseni_username): 
    if uneseni_username in korisnici.keys(): 
        uneseni_password = input('Unesi lozinku: ')
        if uneseni_password == korisnici[uneseni_username]['lozinka']:
            print(f"Dobrodošli, {korisnici[uneseni_username]['ime']} {korisnici[uneseni_username]['prezime']}")
            izbornik2(uneseni_username)

        else: 
            print('Pogrešna lozinka!')
            logiranje(uneseni_username)
    else: 
        print(f'Nepostojeće korisničko ime!')

def otvaranje_racuna(): 
    k_ime = input('Unesite username: ')
    ime = input('Unesite Vaše ime: ')
    prezime = input('Unesite Vaše prezime: ')
    lozinka = input('Unesite lozinku: ')
    korisnici[k_ime] = {'ime': ime, 'prezime': prezime, 'lozinka': lozinka, 'stanje': 0, 'promet':[]}
    izbornik2(k_ime)

def prikaz_stanja(uneseni_username):
    print(f"Stanje Vašeg računa iznosi: {korisnici[uneseni_username]['stanje']}€")

def prikaz_stanja2(uneseni_username):
    print(f"Stanje Vašeg računa iznosi: {korisnici[uneseni_username]['stanje']}€")
    izbornik2(uneseni_username)
    

def polog(uneseni_username):
    iznos_pologa = int(input('Unesite iznos pologa: '))
    korisnici[uneseni_username]['stanje'] = korisnici[uneseni_username]['stanje'] + iznos_pologa
    prikaz_stanja(uneseni_username)
    sat = dt.datetime.now().hour
    minuta = dt.datetime.now().minute
    dan = dt.datetime.now().day
    mjesec = dt.datetime.now().month
    godina = dt.datetime.now().year
    vrijeme_transakcije = f'{dan}.{mjesec}.{godina}. u {sat}:{minuta}'
    obavljeni_promet = {'vrijeme': vrijeme_transakcije, 'polog': iznos_pologa, 'trenutno stanje' : korisnici[uneseni_username]['stanje']}
    
    korisnici[uneseni_username]['promet'].append(obavljeni_promet)
    izbornik2(uneseni_username)

def podizanje(uneseni_username):
    podignuti_iznos = int(input('Unesite iznos koji želite podignuti: '))
    korisnici[uneseni_username]['stanje'] = korisnici[uneseni_username]['stanje'] - podignuti_iznos
    prikaz_stanja(uneseni_username)
    sat = dt.datetime.now().hour
    minuta = dt.datetime.now().minute
    dan = dt.datetime.now().day
    mjesec = dt.datetime.now().month
    godina = dt.datetime.now().year
    vrijeme_transakcije = f'{dan}.{mjesec}.{godina}. u {sat}:{minuta}'
    obavljeni_promet = {'vrijeme': vrijeme_transakcije, 'polog': -podignuti_iznos, 'trenutno stanje' : korisnici[uneseni_username]['stanje']}

    korisnici[uneseni_username]['promet'].append(obavljeni_promet)
    izbornik2(uneseni_username)

def prikaz_prometa(uneseni_username):
    for v in korisnici[uneseni_username]['promet']:
        if v['polog'] >= 0: 
            print(f"{v['vrijeme']} uplaćen je iznos od {v['polog']}€")
        if v['polog'] < 0: 
            print(f"{v['vrijeme']} isplaćen je iznos od {-v['polog']}€")
    izbornik2(uneseni_username)


def izbornik2(uneseni_username): 
    odabir_u_računu = input('Odaberite jednu od sljedećih opcija: \n\t 1) Prikaz stanja računa \n\t 2) Polog novca na račun \n\t 3) Podizanje novca sa računa \n\t 4) Prikaz prometa po računu \n\t 5) Izlaz iz računa \n\t')
    if odabir_u_računu == '1':
        prikaz_stanja2(uneseni_username)
    if odabir_u_računu == '2':
        polog(uneseni_username)
    if odabir_u_računu == '3':
        podizanje(uneseni_username)
    if odabir_u_računu == '4':
        prikaz_prometa(uneseni_username)
    if odabir_u_računu == '5':
        izbornik()


izbornik()
#print(korisnici)