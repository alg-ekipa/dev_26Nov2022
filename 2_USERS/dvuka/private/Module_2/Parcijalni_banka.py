administrator={ 
    'anam':['Ana','Mihaljevic', 'aei123'],
    'gork':['Goran', 'Kolar', 'bei456']}

def logiranje(uneseni_username):
    while uneseni_username not in administrator.keys():
        uneseni_username=input('Uneseno korisničko nije administrator! Unesi korisničko ime administratora: ')
    else:    
        uneseni_pass=input('Unesi lozinku: ')
        while uneseni_pass!=administrator[uneseni_username][2]:
            print('Pogrešna lozinka!')
            uneseni_pass=input('Unesi lozinku: ')
        else:
            print(f'Dobro došli, {administrator[uneseni_username][0]} {administrator[uneseni_username][1]}!')
    print()
racuni = {
    '0001': {'naziv': 'Trotter Independent d.o.o.', 'stanje': 5000, 'transakcije': []},
    '0002': {'naziv': 'Algebra d.d.', 'stanje': 10000, 'transakcije': []},
    '0003': {'naziv': 'Vrapčester United', 'stanje': 7500, 'transakcije': []}
}
def ispisi_izbornik():
    print("Izbornik:")
    print("1. Otvaranje računa tvrtke")
    print("2. Prikaz stanja računa")
    print("3. Prikaz prometa po računu")
    print("4. Polog novca na račun")
    print("5. Podizanje novca s računa")
    print("6. Izlaz iz programa")


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
    print("Unesite iznos koji želite položiti na račun:")
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna not in racuni:
        print("Račun s tim brojem ne postoji.")
        return
    iznos = float(input("Unesite iznos pologa: "))
    racuni[broj_racuna]['stanje'] += iznos
    racuni[broj_racuna]['transakcije'].append(f"Polog: +{iznos} kn")
    print(f"Uspješno ste uplatili {iznos} kn na račun.")


def podizanje():
    print("Unesite iznos koji želite podići s računa:")
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna not in racuni:
        print("Račun s tim brojem ne postoji.")
        return
    iznos = float(input("Unesite iznos za podizanje: "))
    stanje = racuni[broj_racuna]['stanje']


while True:
    ispisi_izbornik()
    opcija = input("Odaberite opciju (1-6): ")
    
    if opcija == "1":
        otvori_racun()
    elif opcija == "2":
        prikazi_stanje()
    elif opcija == "3":
        prikazi_promet()
    elif opcija == "4":
        polog()
    elif opcija == "5":
        podizanje()
    elif opcija == "6":
        print("Hvala što ste koristili naš program!")
        break
    else:
        print("Neispravan odabir, molimo pokušajte ponovo.")

ispisi_izbornik()
otvori_racun()
prikazi_stanje()
prikazi_promet()
polog()
podizanje()
