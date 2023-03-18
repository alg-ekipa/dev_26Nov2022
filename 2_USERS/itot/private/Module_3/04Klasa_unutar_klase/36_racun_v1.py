'''Klasa Racun:
• Broj računa
• Datum izdavanja
• Lista stavki:
• Redni broj – Proizvod 1 – cijena
• Redni broj – Proizvod 2 – cijena
• …
• Iznos PDV-a
• Ukupan iznos
• Funkcije:
• Obračunaj PDV
• Izračunaj ukupan iznos
• Ispiši račun
• Promijeni stavku
• Izbaci stavku'''

import datetime

'''class Racun:
    def __init__(datum, ):
        self.datum
    
    class Datum_izdavanja:
    def __init__(self, dan, mjesec, godina):
        self.dan = dan
        self.mjesec = mjesec
        self.godina = godina
        godina = int(datetime.date.today()[0:4])
'''
danas = list(datetime.date.today())

print(danas)
print(danas[0:3])