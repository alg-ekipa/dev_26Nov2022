import os

korisnici = {
    "00001" :["Mak d.o.o.", "236000012345678", 50000],
    "00002": ["Sunset d.o.o.", "236000098765432", 15000], 
}

saldo = {
    "00001":["50000"],
    "00002":["100000"]
}

administrator = {
    "admin": ["Luka Lukic", "98765"]
}
#print(korisnici)

def pregled_korisnika():
    for korisnik in korisnici.values():
        print(korisnik[0], korisnik[1], korisnik[2])
#pregled_korisnika()
        print()

def logiranje(username):
    if username in administrator.keys():
        while True:
            password = input("Unesi lozinku: ")
            if password == administrator[username][1]:
                print(f"\nDobrodosli {administrator[username][0]}")
                print()
                break
            else:
                print("Pogrešna lozinka.")
    else:
        print("Nepostojeće koricničko ime.")
        print()
        

def novi_korisnik():
    sifra = input("Unesi sifru korisnika: ")
    while len(sifra) != 5:
        print("Sifra korisnika mora sadrzavati 5 znamenki.")
        sifra = input("Ponovo unesi sifru korisnika: ")
    else:
        naziv = input("Unesi naziv poduzeća: ")
        racun = input("Unesi broj računa: ")
        while len(racun) != 15:
            print("Broj računa mora sadržavati 15 znamenki.")
            racun = input("Ponovo unesi broj računa: ")
        saldo = input("Unesi saldo računa: ")
        korisnici[sifra] = [naziv, racun, saldo]
        print()
        print("Korisnici u bazi: ")
        pregled_korisnika()  
#novi_korisnik()
print()

def stanje_racuna():
    for kljuc, vrijednost in korisnici.items():
        print(korisnici[kljuc][2])
#stanje_racuna()
print()

def uplata():
    uplata = float(input("Upisite iznos za uplatu: "))
    novo_stanje = korisnici[racun][-1] + uplata
    korisnici[racun].append(novo_stanje)
    print(f"Na racunu: {racun}  novo stanje je: {novo_stanje} Eur.")
    print()

def isplata():
    isplata = float(input("Upisi iznos koji želite isplatiti: "))
    podizanje_stanje = korisnici[racun][-1] - isplata
    korisnici[racun].append(podizanje_stanje)
    print(f"Na racunu {racun} sada se nalazi {podizanje_stanje} Eur.")
    print()

def prikaz_prometa():
    a = len(korisnici[racun]) -1
    for i in range(a, 2, -1):
        print(f"\t\tStanje:\t\tUplata/isplata:\n\t\t{korisnici[racun][i]} eura\t\t {korisnici[racun][i]-korisnici[racun][i-1]} Eur.')")


while 1:
    prijava = input("Unesite username administratora: ")
    logiranje(prijava)
    if prijava == "admin":
        izbornik = int(input("Odaberite opciju:\n1. Pregled korisnika\n2. Uplata/Isplata\n3. Novi korisnik\n4. Odjava\n-----> "))
        if izbornik == 1:
            pregled_korisnika()
            continue
        elif izbornik == 2:
            racun = input("Unesite šifru korisnika za uplatu/isplatu: ")
            while racun not in korisnici.keys():
                racun = input("Korisnik ne postoji. Unesite ispravanu šifru korisnika: ")
            else:
                while True:
                    izbor = int(input("1. Uplata\n2. Isplata ---> "))
                    if izbor == 1:
                        uplata()
                    elif izbor == 2:
                        isplata()
                        continue
        elif izbornik == 3:
            novi_korisnik()
            continue
        elif izbornik == 4:
            quit()
    else:
        print("Niste odabrali valjanu opciju.")
        izbornik = int(input("Odaberite opciju:\n1. Pregled korisnika\n2. Uplata/Isplata\n3. Novi korisnik\n4. Odjava\n-----> "))
            

    


            