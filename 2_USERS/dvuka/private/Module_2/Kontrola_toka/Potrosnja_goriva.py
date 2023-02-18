def kilometri():
    izračun = budžet_gorivo/potrosnja_goriva/cijena_goriva*100
    prelazak = f'Sa budžetom od {budžet_gorivo}€ mjesečno možeš prijeći {izračun}km, ako je cijena goirva {cijena_goriva}€ i prosječna potrošnja {potrosnja_goriva}'
    return prelazak


budžet_gorivo = float(input('Koliki je mjesečni budžet € za gorivo:'))
potrosnja_goriva = float(input('Unesite kolika je prosječna potrošnja goriva automobila: '))
cijena_goriva = float(input('Koliko košta litra goriva: '))
    
print(kilometri())