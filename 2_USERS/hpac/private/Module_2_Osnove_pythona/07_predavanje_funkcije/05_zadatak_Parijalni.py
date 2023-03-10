''' Program za sada izvršava u konzoli
Funkcionalnosti:
• Izbornik
- pregled klijenata
• Otvaranje računa tvrtke
• Prikaz stanja računa
• Prikaz prometa po računu
• Polog novca na račun
• Podizanje novca s računa
• Izlaz iz programa (program se nakon
svake akcije vrati na početni izbornik
u kojem postoji opcija Izlaz)'''

klijenti = {
    'Ajmo d.o.o.' : ['Ilica 35','Zagreb','12345678912'],
    'Sedam d.o.o.' : ['Zagrebačka 22','Osijek','74125896321'],
    'Kuda d.o.o.' : ['Lijevo 11','Karlovac','32165498741']
}

računi = {
    'Ajmo d.o.o.' : [38,41,10,23,7,-25,-18,22],
    'Sedam d.o.o.' : [36,74,61,24,8,-32,-18,27,4,-8],
    'Kuda d.o.o.' : [-13,25,63,-41,27,13,8,2,36]
}

def otvaranje_racuna():
    #Otvaranje računa za novog klijenta, definira se ident(key), te ime, prezime, i šifra (values)
    naziv = input('Unesite NAZIV za nove firme: ')
    while len(naziv) <=2:
        naziv = input('Uneseni NAZIV je prekratak!! Mora imati minimalno 3 slova.\n Unesite NAZIV nove firme: ')
    adresa = input('Unesite AFRESU nove firme: ')
    while len(adresa) <=2:
        adresa = input('Unesena ADRESA je prekratka!! Mora imati minimalno 3 slova.\n Unesite ADRESU nove firme: ')
    grad = input('Unesite GRAD u kojem se nalazi firma: ')
    while len(grad) <=2:
        grad = input('Uneseni podatak nije doba!! Mora imati minimalno 3 slova.\n Unesite PREZIME novog klijenta: ')
    oib = input('Unesite OIB za novog kornisika: ')
    while len(oib) !=11 : #OIB mora biti točna 11 brojeva inače ga ne prihvaća
        oib = input('Uneseni OIB nije dobar!! Mora imati točno 11 brojeva.\n Unesite OIB novog klijenta: ')
        klijenti[naziv] = [adresa, grad, oib]
    print(klijenti)

#otvaranje_racuna()

def pregled_klijenti():
    for k,v in klijenti.items():
        print(k,'-',v[0],',',v[1],',','OIB:',v[2]) #ispiuje k - ključ (naziv) firme i v (values) adresa, grad, OIB - pomoću stringova unutar printa dobije zareze i natpis OIB

#pregled_klijenti()

def stanje_računa():
   for k, v in računi.items():
       print({k:sum(map(int, v))}) #zbraja sve promete unutar računa, koji su zadani

#stanje_računa()

def prikaz_prometa():
    for k, v in računi.items():
        print(k,':',v)

#prikaz_prometa()

def prometi_na_računu ():
    firma = input ('Unesite ime firmu na čiji račun želite položiti novac: ')
    while firma not in računi:
        firma = input('Unešena firma nije klijent!! Molim pokušajte ponovno: ')
    else:
        uplata = float(input('Unesite iznos koji želite položiti na račun:'))
        računi[firma].append(uplata)

#prometi_na_računu()


def odjava():
    print('Hvala na korištenju!')



def izbornik():
    print('Izbornik mogućih radnji za klijenta:')
    print('1. Pregled klijenata')
    print('2. Pregled stanja računa')
    print('3. Prikaz prometa po računu')
    print('4. Polaganje/dizanje novca sa računa')
    print('5. Dodavanje novog klijenta')
    print('6. Odjava')
    odabir = int(input('Što želite napraviti: '))
    if odabir == 1:
        pregled_klijenti()
        print()
        izbornik()
    elif odabir == 2:
        stanje_računa()
        print()
        izbornik()
    elif odabir == 3:
        prikaz_prometa()
        print()
        izbornik()
    elif odabir == 4:
        prometi_na_računu()
        print()
        izbornik()
    elif odabir == 5:
        otvaranje_racuna()
        print()
        izbornik()
    elif odabir == 6:
        odjava()
    else:
        print('Napravili ste neispravan unos!! Molim pokušajte ponovno!!')
        izbornik()

izbornik()