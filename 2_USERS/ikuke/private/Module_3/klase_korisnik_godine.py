import datetime
import datetime as dt 

print(dt.datetime.now())
sat = dt.datetime.now().hour
minuta = dt.datetime.now().minute

godina = dt.datetime.now().year


# kreirati klasu korisnik koja ima podatke ime, prezime, godinu rođenja

# ime i prezime unosi se kao jedna varijabla koja se kasnije razdvaja

# na kraju svega kreirati par objekata i pozivati metodu i ispisati starost korisnika 

lista_objekata=[]

rjecnik_korisnika = {
    0: ["ime", "prezime", "godina_rodjenja"]
}

brojac=1

class Korisnik():
    def __init__(self):
        imeprezime=input('Unesi ime i prezime korisnika: ')
        godina_rodjenja=input('Unesi godinu rodjenja korisnika:')
        imeprezime=imeprezime.split()
        self.ime=imeprezime[0]
        self.prezime=imeprezime[1]
        try:
            self.godina_rodjenja=int(godina_rodjenja)
        except:
            self.godina_rodjenja=int(1900)
        print(self.ime)
        print(self.prezime)
        print(self.godina_rodjenja)
        return None

    def vrati_ime(self):
        return self.ime

    def vrati_prezime(self):
        return self.prezime

    def vrati_starost(self):
        return (godina-self.godina_rodjenja)

while True:

    if input("unesite korisnika? - enter za kraj "):
        korisnik=Korisnik() 
        lista_objekata.append(korisnik)

    elif input("ispis korisnika? - enter za kraj "):
        for korisnik in lista_objekata:
            print(korisnik.vrati_ime(), korisnik.vrati_prezime(), "je star ", korisnik.vrati_starost(), "godina")

    else:
        break

        









