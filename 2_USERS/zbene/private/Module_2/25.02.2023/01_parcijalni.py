#Napravite program za rad na pultu u banci
#Program za sada izvršava u konzoli funkcionalnosti:
#1. Izbornik
#2. Otvaranje računa tvrtke
#3. Prikaz stanja računa
#4. Prikaz prometa po računu
#5. Polog novca na račun
#6. Podizanje novca s računa
#7. Izlaz iz programa (program se nakon svake akcije vrati na početni izbornik u kojem postoji opcija Izlaz)

korisnici = {
    'osobni bankar' : ['Nisamja', 'Robot', '2705', 'bankarski savjetnik'],
    'pripravnik' : ['Jasampočetnik', 'Naalgebri', '0909', 'pripravnici']
}

klijenti = {
      '11111111111' : {
    'naziv_tvrtke' : 'Mali mrav d.o.o.',
    'adresa_tvrtke' : 'Nemam ulicu 2',
    'sjedište_tvrtke' : 'Nemam PB ni grad',
    'stanje_računa' : 2654.46,
    'promet_po_računu' : []
      }
}

#print(korisnici)
#print(klijenti)


def login(): #0#
    broj_pokušaja = 0
    print('\nBanka X d.d., hvala na službi.\n')
    while broj_pokušaja < 3:
        korisničko_ime = input ('Unesi korisničko ime (max 3 pokušaja): ')
        zaporka = input ('Unesi zaporku (max 3 pokušaja): ')
        if korisničko_ime in korisnici.keys() and korisnici[korisničko_ime] [2] == zaporka:
            print(f'\nDobrodošli, {korisnici[korisničko_ime] [0]} {korisnici[korisničko_ime] [1]}')
            break       
        else:
            broj_pokušaja +=1
            print ('\nNiste upisali dobro korisničko ime ili zaporku, pokušajte ponovo.\n')
    if broj_pokušaja == 3:
        print('\nTri neuspjela pokušaja prijave. Račun je blokiran!\n')

#login()


def otvaranje_računa(): #1#
    OIB = input ('Unesi OIB (11 brojeva) tvrtke kao novog klijenta: ')
    while len (OIB) !=11 or not OIB.isdigit():
        OIB = input('\nUneseni OIB ne sadrži 11 brojeva ili nije ispravnog formata, pokušajte ponovo: ')
    if OIB in klijenti.keys():
        print ('\nTvrtka već ima postojeći račun!\n')
        return 
    naziv_tvrtke = input ('Unesi naziv tvrtke (minimalno 7 znakova) kao novog klijenta: ')
    while len (naziv_tvrtke) < 7:
        naziv_tvrtke = input('Naziv tvrtke je kraći od 7 znakova, pokušajte ponovo: ')
    adresa_tvrtke = input ('Unesi adresu (minimalno 5 znakova) tvrtke kao novog klijenta: ')
    while len (adresa_tvrtke) < 5:
        adresa_tvrtke = input ('Unesena adresa ne sadrži minimalno 5 znakova, pokušajte ponovo: ')
    sjedište_tvrtke = input ('Unesi sjedište (PB, Grad) (minimalno 9 znakova) tvrtke kao novog klijenta: ')
    while len (sjedište_tvrtke) < 9:
        sjedište_tvrtke = input ('Uneseno sjedište (PB, Grad) ne sadrži minimalno 9 znakova, pokušajte ponovo: ')
    stanje_računa = input('Unesi iznos stanja računa: ')
    while not stanje_računa.isdigit() or int (stanje_računa) < 0:
        stanje_računa = input ('Uneseni iznos stanja računa nije broj ili je manji od 0,00 EUR, pokušajte ponovo: ')
        
    stanje_računa = int (stanje_računa)
    
    klijenti[OIB] = {'naziv_tvrtke': naziv_tvrtke, 'adresa_tvrtke': adresa_tvrtke, 'sjedište_tvrtke' : sjedište_tvrtke, 'stanje_računa' : stanje_računa, 'promet_po_računu' : []}
    print (f'\nUspješno otvoren račun za tvrtku {naziv_tvrtke}.\n')

#otvaranje_računa()
                       

def prikaz_stanja_računa(): #2#
    OIB = input ('\nUnesi OIB (11 brojeva) tvrtke za prikaz stanja računa: ')
    while len (OIB) != 11 or not OIB.isdigit():
        OIB = input ('\nUneseni OIB ne sadrži minimalno 11 brojeva ili nije ispravnog formata, pokušajte ponovo: ')
    if OIB not in klijenti:
        print (f'\nTvrtka s navedenim OIB-om {OIB} ne postoji!\n')
        return
    for k, v in klijenti.items():
        if k == OIB:
            print (f"\n Trenutno stanje računa tvrtke {v['naziv_tvrtke']} iznosi EUR {v['stanje_računa']}\n")
            return
    
#prikaz_stanja_računa()


def prikaz_prometa_po_računu(): #3#
    OIB = input('\nUnesi OIB (11 brojeva) tvrtke za pregled prometa po računu: ')
    while len (OIB) !=11 or not OIB.isdigit():
        OIB = input ('\nUneseni OIB ne sadrži minimalno 11 brojeva ili nije ispravnog formata, pokušajte ponovo: ')
    if OIB not in klijenti:
        print('\nTvrtka s unesenim OIB-om ne postoji!\n')
        return
    
    promet_po_računu = klijenti[OIB]['promet_po_računu']
    if not promet_po_računu:
        print('\nNa računu nema zabilježenog prometa.\n')
        return
    
    print(f"Promet na računu za tvrtku {klijenti[OIB]['naziv_tvrtke']}:")
    for popis_transakcija in promet_po_računu:
        print(popis_transakcija)

#prikaz_prometa_po_računu()


def polog_novca_na_račun(): #4#
    OIB = input('\nUnesi OIB (11 brojeva) tvrtke za polog novca na račun: ')
    while len (OIB) !=11 or not OIB.isdigit():
        OIB = input ('\nUneseni OIB ne sadrži minimalno 11 brojeva ili nije ispravnog formata, pokušajte ponovo: ')
    if OIB not in klijenti:
        print('\nTvrtka s unesenim OIB-om ne postoji!\n')
        return
    
    iznos = input ('\nUnesi iznos pologa novca na račun tvrtke: ')
    while not iznos.replace ('.', '',1).isdigit() or float(iznos) <=0:
        iznos = input ('Uneseni iznos nije broj ili je negativan ili jednak 0,00 EUR, pokušajte ponovo: ')
    iznos = round(float(iznos),2)

    klijenti[OIB] ['stanje_računa'] += iznos
    klijenti[OIB] ['promet_po_računu'].append (f'Uplata: + {iznos} EUR.')
    print (f"\nNa račun tvrtke {klijenti [OIB]['naziv_tvrtke']} uplaćeno {iznos} EUR.\n")

#polog_novca_na_račun()

def podizanje_novca_sa_računa(): #5#
    OIB = input('\nUnesi OIB (11 brojeva) tvrtke koja želi podići novac sa računa: ')
    while len(OIB) != 11 or not OIB.isdigit():
        OIB = input('\nUneseni OIB ne sadrži minimalno 11 brojeva ili nije ispravnog formata, pokušajte ponovo: ')
    if OIB not in klijenti:
        print('\nTvrtka s unesenim OIB-om ne postoji!\n')
        return

    stanje_računa = klijenti[OIB]['stanje_računa']
    if stanje_računa <= 0:
        print('\nNa računu tvrtke nema dovoljno sredstava za isplatu.\n')
        return

    isplata = input('\nUnesi iznos isplate novca sa računa tvrtke: ')
    while not isplata.replace('.', '', 1).isdigit() or float(isplata) <= 0 or float(isplata) > stanje_računa:
        isplata = input('Uneseni iznos nije broj ili je negativan, ili je veći od stanja računa, pokušajte ponovo: ')
    isplata = round(float(isplata), 2)

    klijenti[OIB]['stanje_računa'] -= isplata
    klijenti[OIB]['promet_po_računu'].append(f'Isplata: -{isplata} EUR.')
    print(f"\nSa računa tvrtke {klijenti[OIB]['naziv_tvrtke']} je isplaćeno {isplata} EUR.\n")

#podizanje_novca_sa_računa()

def izbornik():
    print('\nBanka X d.d.\n')
    print('1. Otvaranje računa')
    print('2. Prikaz stanja računa')
    print('3. Prikaz prometa po računu')
    print('4. Polog novca na račun')
    print('5. Podizanje novca sa računa')
    print('6. Izlaz iz programa')

    odabir = input('\nOdaberite broj funkcije koju želite izvršiti: ')

    if odabir == '1':
        otvaranje_računa()
        izbornik()
    elif odabir == '2':
        prikaz_stanja_računa()
        izbornik()
    elif odabir == '3':
        prikaz_prometa_po_računu()
        izbornik()
    elif odabir == '4':
        polog_novca_na_račun()
        izbornik()
    elif odabir == '5':
        podizanje_novca_sa_računa()
        izbornik()
    elif odabir == '6':
        print('\nHvala ti na marljivom radu. Doviđenja!\n')
    else:
        print('\nUnijeli ste neispravan odabir. Pokušajte ponovno.')
        izbornik()

izbornik()