korisnici = {'Marko': {'broj_racuna': '123456789', 'stanje_racuna': 5000},
             'Ivana': {'broj_racuna': '987654321', 'stanje_racuna': 10000},
             'Petar': {'broj_racuna': '567890123', 'stanje_racuna': 7500}}

# Glavna petlja programa
while True:
    # Prikaži izbornik
    print('Izbornik:')
    print('1 - Ispis stanja računa')
    print('2 - Uplata na račun')
    print('3 - Isplata sa računa')
    print('4 - Izlaz')

    # Dohvati odabir korisnika
    odabir = input('Odaberi opciju: ')

    # Obradi odabir korisnika
    if odabir == '1':
        # Ispis stanja računa
        ime = input('Unesite ime korisnika: ')
        if ime in korisnici:
            stanje = korisnici[ime]['stanje_racuna']
            print(f'Stanje računa za korisnika {ime} je {stanje} kn.')
        else:
            print(f'Korisnik {ime} nije pronađen u bazi podataka.')

    elif odabir == '2':
        # Uplata na račun
        ime = input('Unesite ime korisnika: ')
        if ime in korisnici:
            iznos = float(input('Unesite iznos uplate: '))
            korisnici[ime]['stanje_racuna'] += iznos
            print(f'Uspješno ste uplatili {iznos} kn na račun korisnika {ime}.')
        else:
            print(f'Korisnik {ime} nije pronađen u bazi podataka.')

    elif odabir == '3':
        # Isplata sa računa
        ime = input('Unesite ime korisnika: ')
        if ime in korisnici:
            iznos = float(input('Unesite iznos isplate: '))
            if iznos > korisnici[ime]['stanje_racuna']:
                print('Nemate dovoljno sredstava na računu.')
            else:
                korisnici[ime]['stanje_racuna'] -= iznos
                print(f'Uspješno ste isplatili {iznos} kn sa računa korisnika {ime}.')
        else:
            print(f'Korisnik {ime} nije pronađen u bazi podataka.')

    elif odabir == '4':
        # Izlaz iz programa
        print('Hvala što ste koristili našu banku.')
        break

    else:
        # Neispravan odabir korisnika
        print('Neispravan odabir. Molimo pokušajte ponovno.')

# Dohvaćanje podataka o računima iz baze podataka
racuni = {
    '0001': {'naziv': 'Tvrtka A', 'stanje': 5000, 'transakcije': []},
    '0002': {'naziv': 'Tvrtka B', 'stanje': 10000, 'transakcije': []},
    '0003': {'naziv': 'Tvrtka C', 'stanje': 7500, 'transakcije': []}
}

def otvori_racun():
    broj_racuna = input("Unesite broj računa (4 znamenke): ")
    if broj_racuna in racuni:
        print("Račun s tim brojem već postoji.")
        return
    naziv = input("Unesite naziv tvrtke: ")
    stanje = float(input("Unesite početno stanje na računu: "))
    racuni[broj_racuna] = {'naziv': naziv, 'stanje': stanje, 'transakcije': []}
    print(f"Račun za tvrtku {naziv} uspješno otvoren.")

def prikazi_stanje():
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna not in racuni:
        print("Račun s tim brojem ne postoji.")
        return
    stanje = racuni[broj_racuna]['stanje']
    print(f"Trenutno stanje na računu {broj_racuna} je {stanje} kn.")

def prikazi_promet():
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna not in racuni:
        print("Račun s tim brojem ne postoji.")
        return
    transakcije = racuni[broj_racuna]['transakcije']
    for i, transakcija in enumerate(transakcije):
        print(f"{i+1}. {transakcija}")

def polog():
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna not in racuni:
        print("Račun s tim brojem ne postoji.")
        return
    iznos = float(input("Unesite iznos pologa: "))
    racuni[broj_racuna]['stanje'] += iznos
    racuni[broj_racuna]['transakcije'].append(f"Polog: +{iznos} kn")
    print(f"Uspješno ste uplatili {iznos} kn na račun.")

def podizanje():
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna not in racuni:
        print("Račun s tim brojem ne postoji.")
        return
    iznos = float(input("Unesite iznos za podizanje: "))
    stanje = racuni[broj_racuna]['stanje']

otvori_racun()
prikazi_stanje()
prikazi_promet()
polog()
podizanje()