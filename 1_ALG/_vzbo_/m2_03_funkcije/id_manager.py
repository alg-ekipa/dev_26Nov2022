korisnici = {
    "admin" : ["Zvonimir", "Hadžić", "admin"],
}

def isAdmin(username):
    if (username == "admin"): return True

def userExists(username):
    if username in korisnici:
        return True

def ispisiAdminKomande():
    print("\nKomandna lista:")
    print("add - dodavanje korisnika")
    print("delete - brisanje korisnika")
    print("logout - izlaz iz trenutnog računa")
    print("list - lista postojećih korisnika")
    print("exit - izlaz iz programa")

def main():
    trenutniKorisnik = ""
    while(trenutniKorisnik == ""):
        username = input("\nUnesite vaše korisničko ime: ")
        if userExists(username):
            lozinka = input("Molimo unesite vašu lozinku: ")
            if (lozinka == korisnici[username][2]):
                trenutniKorisnik = username
                print(f"\nDobro došli {korisnici[username][0]} {korisnici[username][1]}!")
                if (isAdmin(username)):
                    ispisiAdminKomande()
            else:
                print("Nažalost lozinka je netočna")
        else:
            print(f"Korisnik '{username}' ne postoji")

    # petlja je završila ovdje jer je korisnik trenutno ulogiran
    while(trenutniKorisnik):
        if isAdmin(trenutniKorisnik):
            print("\nUnesite vašu naredbu, koristite 'help' za pomoć oko komandi")
            print(f"trenutniKorisnik = {trenutniKorisnik}")
            unos = input("> ")
            if (unos == "help"):
                ispisiAdminKomande()
            elif(unos == "add"):
                username = input("Unesite username: ")
                if (username and len(username) > 0):
                    ime = input("Unesite ime: ")
                    if not userExists(username):
                        if (ime and len(ime) > 0):
                            prezime = input("Unesite prezime: ")
                            if (prezime and len(prezime) > 0):
                                sifra = input("Unesite šifru: ")
                                if (sifra and len(sifra) > 0):
                                    korisnici[username] = [ime, prezime, sifra]
                                    print(f"Korisnik {username} uspješno dodan!")
                                else:
                                    print("Šifra mora biti valjana! Molim krenite ispočetka")
                            else:
                                print("Prezime mora biti valjano! Molim krenite ispočetka")
                        else:
                            print("Ime mora biti valjano! Molim krenite ispočetka")
                    else:
                        print("Taj korisnik već postoji!")
                else:
                    print("Username mora biti valjan! Molim krenite ispočetka")

            elif(unos == "delete"):
                username = input("Molimo unesite username: ")
                if (username and len(username) > 0):
                    if userExists(username):
                        if (username == "admin"):
                            print("Nije moguće izbrisati administrativni račun! Zamislite samo katastrofu!")
                        else:
                            korisnici.pop(username)
                            print(f"Korisnik '{username}' uspješno izbrisan!")
                    else:
                        print(f"Korisnik '{username}' ne postoji!")
                else:
                    print("Username mora biti valjan! Molimo krenite ispočetka!")
            elif (unos == "logout"):
                trenutniKorisnik = ""
                main()
            elif (unos == "list"):
                print("\nPostojeći korisnici:")
                for x in korisnici.keys():
                    print(x)
            elif (unos == "exit"):
                quit() # mora quit jer ako koristimo return a korisnik je vise puta napravio logout, onda ce morati višestruko exit naredbu davati da izađe iz svih main funkcija koje je otvorio sa logout
            else:
                print(f"Nepoznata komanda '{unos}'")
        else:
            # korisnik nije admin
            print("Trenutno kao normalni korisnik možete samo koristiti logout i exit komande")
            komanda = input("> ")
            if (komanda == "logout"):
                trenutniKorisnik = ""
                main()
            elif (komanda == "exit"):
                quit()
    


main()