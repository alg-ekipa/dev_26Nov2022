class Zaposlenik:
    def __init__(self, ime, prezime, email, mobitel):
        self.ime = ime
        self.prezime = prezime
        self.email = email
        self.mobitel = mobitel

    def ispis(self):
        return(
            f"Ime: {self.ime}\n"
            f"Prezime: {self.prezime}\n"
            f"Mail: {self.email}\n"
            f"Mobitel: {self.mobitel}\n"
        )

    def promjena_emaila(self, novi_mail):
        self.email = novi_mail
        return "eMail uspješno promjenjen."
    
    def promjena_mobitela(self, novi_mobitel):
        self.mobitel = novi_mobitel
        return "Broj mobitela uspješno promijenjen."
    
def main():
    zaposlenik1 = Zaposlenik("Petar", "Petrić", "pp@mail.com", "098123456")

    print("Dostupni podaci o zaposleniku: ")
    print(zaposlenik1.ispis())

    print(zaposlenik1.promjena_emaila("petar@mail.com"))
    print(zaposlenik1.promjena_mobitela("09812121212"))

    print("n\Ažurirani podaci o zaposleniku broj 1.")
    print(zaposlenik1.ispis())

if __name__ == "__main__":
    main()





