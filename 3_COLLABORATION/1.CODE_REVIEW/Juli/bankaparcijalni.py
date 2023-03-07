import os

korisnici = {
    "00001" :["Mak d.o.o.", "236000012345678", 50000,'password'],
    "00002": ["Sunset d.o.o.", "236000098765432", 15000,'password'], 
}


poslovni_korisnici = {}

administrator = {
    "admin": ["Luka Lukic", "98765"]
    
}
#print(korisnici)

def pregled_korisnika():
    for korisnik in korisnici.values():
        print(korisnik[0], korisnik[1], korisnik[2])
        print()

def logiranje_admin(username):
    if username in administrator.keys():
        password = input("Unesi lozinku: ")
        if password == administrator[username][1]:
            print(f"\nDobrodosli {administrator[username][0]}")
            return True
        else:
            print("Pogrešna lozinka.")
            return False
    else:
        print("Nepostojeće koricničko ime.")
        return False
        
def logiranje_korisnik(username):
    if username in korisnici.keys():
        password = input("Unesi lozinku: ")
        if password == korisnici[username][3]:
            print(f"\nDobrodosli {korisnici[username][0]}")
            return True
        else:
            print("Pogrešna lozinka.")
            return False
    else:
        print("Nepostojeće koricničko ime.")
        return False

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

# def stanje_racuna():
#     for kljuc, vrijednost in korisnici.items():
#         print(korisnici[kljuc][2])
# #stanje_racuna()
# print()

# def uplata():
#     uplata = float(input("Upisite iznos za uplatu: "))
#     novo_stanje = korisnici[racun][-1] + uplata
#     korisnici[racun].append(novo_stanje)
#     print(f"Na racunu: {racun}  novo stanje je: {novo_stanje} Eur.")
#     print()

# def isplata():
#     isplata = float(input("Upisi iznos koji želite isplatiti: "))
#     podizanje_stanje = korisnici[racun][-1] - isplata
#     korisnici[racun].append(podizanje_stanje)
#     print(f"Na racunu {racun} sada se nalazi {podizanje_stanje} Eur.")
#     print()

# def prikaz_prometa():
#     a = len(korisnici[racun]) -1
#     for i in range(a, 2, -1):
#         print(f"\t\tStanje:\t\tUplata/isplata:\n\t\t{korisnici[racun][i]} eura\t\t {korisnici[racun][i]-korisnici[racun][i-1]} Eur.')")

main_menu = True
while main_menu == True:
    odabir_korisnika = input("""
                    Dobrodosli! Molim prijavite se.
                    1) admin
                    2) korisnik
                    = """)
    
    if odabir_korisnika == '1':
        admin_menu = True
        admin_username = input("""Molimo unesite korisnicko imate admina: """)
        if logiranje_admin(admin_username) == True:
            while admin_menu == True:
            
                admin_unos = input('''
                    Odaberite opciju:
                    1. Pregled korisnika
                    2. Uplata/Isplata
                    3. Novi korisnik
                    4. <-- Odjava ''')

                if admin_unos == '1':
                        # admin_unos_korisnika = input("Unosite zeljenog korisnika.") ---> primjer ako zelis vidjeti samo jednog korisnika.
                        pregled_korisnika()
                        admin_menu = True
                        
                if admin_unos == '2':
                    pass
                
                if admin_unos == '3':
                    pass
                
                if admin_unos == '4':
                    admin_menu = False

    if odabir_korisnika == '2':
        korisnik_menu = True
        korisnik_username = input("""Molimo unesite korisnicko imate korisnika: """)
        if logiranje_korisnik(korisnik_username) == True:
            while korisnik_menu == True:
                        
                            korisnik_unos = input('''
                                Odaberite opciju:
                                1. Pregled
                                2. Uplata
                                3. Isplata
                                4. <-- Odjava ''')

                            if korisnik_unos == '1':
                                    # admin_unos_korisnika = input("Unosite zeljenog korisnika.") ---> primjer ako zelis vidjeti samo jednog korisnika.
                                    pregled_korisnika()
                                    admin_menu = True
                                    
                            if korisnik_unos == '2':
                                pass
                            
                            if korisnik_unos == '3':
                                pass
                            
                            if korisnik_unos == '4':
                                korisnik_menu = False


    else:
        admin_menu = False
        


            