korisnici={
    '1001':['Dora Pejacevic','1023456', 10000.00 ],
    '1002':['Zinka Kunc','2345678', 2000.00],
    '1003':['Slava Raškaj', '3456789', 5000.00],
    '1004':['Dora Maar', '4567890', 2500.00]
}

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

def pregled_korisnika():
    print('Broj racuna\t\tNaziv tvrtke\t\tMatični broj\t\tStanje računa')
    for i, j in korisnici.items():
        print(f'{i}:\t\t\t{j[0]}\t\t{j[1]}\t\t\t{j[-1]}')               #zadnje stanje računa se uvijek nalazi na zadnjem mjestu, index [-1]
    print()

def pregled_1_korisnika():
	print(f'Broj racuna: {br_racuna}\nNaziv tvrtke: {korisnici[br_racuna][0]}\nMatični broj: {korisnici[br_racuna][1]}\nStanje racuna: {korisnici[br_racuna][-1]}')

def novi_korisnik():
    br_racuna=input('Unesi broj racuna za novog korisnika: ')
    while br_racuna in korisnici.keys():            # provjera da li vec postoji racun s tim brojem
        print('Broj racuna već postoji!')
        br_racuna=input('Unesi broj racuna: ')
    else:
        ime_tvrtke=input('Unesi ime tvrtke: ')

        MB_tvrtke=input('Unesi jedinstveni maticni broj tvrtke koji ima 7 brojeva: ')   
        while len(MB_tvrtke)!=7:
            MB_tvrtke=input('Uneseni maticni broj tvrtke nema 7 znakova! Pokušajte ponovo: ')
        else:
            for i in korisnici.keys():
                registar_MB=korisnici[i][1]
                #print(registar_MB)
            while MB_tvrtke in registar_MB:                 #provjera da li vec postoji MB
                MB_tvrtke=input('Unesi maticni broj vec postoji! Pokušajte ponovo! ')
            else:
                poc_stanje=float(input('Unesi pocetno stanje racuna tvrtke u eurima: '))
                korisnici[br_racuna] = [ime_tvrtke, MB_tvrtke, poc_stanje]
                print()
                print(f'U bazi se za broj racuna {br_racuna} nalaze sljedeći podaci: \n Naziv tvrtke:\t{ime_tvrtke} \n Matični broj:\t{MB_tvrtke} \n Stanje računa:\t{poc_stanje}')
    print()

def polog_novca():
    polog=float(input('Unesite iznos u eurima koji zelite poloziti na racun: '))
    while polog<0:                  #da li je uneseni broj manji od 0
        polog=float(input('Uneseni iznos nije pozitivan!\nUnesite iznos u eurima koji zelite poloziti na racun: '))
    else:
        novo_stanje=korisnici[br_racuna][-1]+polog
        korisnici[br_racuna].append(novo_stanje)
        print(f'Na br. racuna {br_racuna} se sada nalazi iznos od {novo_stanje} eura.')
        print()

def prikaz_prometa():
    a=len(korisnici[br_racuna])-1
    #print(a)
    for i in range(a,2,-1):
        print(f'\t\tStanje:\t\tUplata/isplata:\n\t\t{korisnici[br_racuna][i]} eura\t\t {korisnici[br_racuna][i]-korisnici[br_racuna][i-1]} eura')

def podizanje_novca():
        podizanje=float(input('Unesite iznos u eurima koji zelite podici s racuna: '))
        while podizanje<0:              #da li je uneseni broj manji od 0
            podizanje=float(input('Uneseni iznos nije pozitivan! Unesite iznos u eurima koji zelite podici s racuna: '))
        else:
            while korisnici[br_racuna][-1]<podizanje:                                 #provjera ima li dovoljno novca na racunu
                podizanje=float(input('Stanje racuna je manje od zeljenog iznosa. Unesite iznos u eurima koji zelite podici s racuna: '))       
            else:
                podizanje_stanje=korisnici[br_racuna][-1]-podizanje
                korisnici[br_racuna].append(podizanje_stanje)
            print(f'Na br. racuna {br_racuna} se sada nalazi iznos od {podizanje_stanje} eura.')
            print()

while 1:
    odg=input('Želite li se prijaviti? da/ne: ')
    if odg=='da':
        unos_user=input('Unesi korisničko ime administora: ')
        logiranje(unos_user)
        while True:
            izbornik=int(input('\n 1. Pregled korisničkih racuna\n 2. Dodavanje novog korisnika \n 3. Pregled/uplata/isplata/prometa po racunu \n 4. Odjava \nUnesite redni broj za željenu radnju:\n'))
            if izbornik==1:
                pregled_korisnika()
            elif izbornik==2:
                novi_korisnik()
            elif izbornik==3:
                br_racuna=input('Unesite br. racuna: ')
                while br_racuna not in korisnici.keys():            #provjera da li postoji navedeni br. racuna
                    br_racuna=input('Uneseni br. racuna ne postoji. \nUnesite br. racuna: ')
                else:
                    while True:
                        izbornik_m=int(input('\n 1. Pregled racuna \n 2. Prikaz prometa po racunu \n 3. Polog novca na racun \n 4. Podizanje novca s racuna \n 5. Izlaz \nUnesite redni broj za željenu radnju:\n'))
                        if izbornik_m==1:
                            pregled_1_korisnika()
                        elif izbornik_m==2:
                            prikaz_prometa()
                        elif izbornik_m==3:
                            polog_novca()
                        elif izbornik_m==4:
                            podizanje_novca()
                        else:
                            break
                    else:
                        break
            else:
                break         
        else:
            break
    else:
        break
   