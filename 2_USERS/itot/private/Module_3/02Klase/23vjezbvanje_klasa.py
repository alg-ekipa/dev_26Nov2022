
class Zaposlenici:

    id_zaposlenika = 0
    iznos_povecanja = 1.04

    def __init__(self,ime,prezime,placa):
        self.ime = ime
        self.prezime = prezime
        self.placa = placa
        self.mail = ime + '.' + prezime + 'mail.com'
        
        Zaposlenici.id_zaposlenika += 1

    def puno_ime(self):
        return '{} {}'.format(self.ime, self.prezime)

    def povecanje_palce(self):
        self.placa = int(self.placa * Zaposlenici.iznos_povecanja)

print(Zaposlenici.id_zaposlenika)

zap_1 = Zaposlenici('Ime1', 'Prezime1', 5500)
zap_2 = Zaposlenici('Ime2', 'Prezime2', 6500)

print(Zaposlenici.id_zaposlenika)