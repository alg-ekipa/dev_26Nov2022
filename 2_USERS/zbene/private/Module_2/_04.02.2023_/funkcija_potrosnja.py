#Izradite aplikaciju za preračunavanje potrošnje goriva automobila u eure uz mogućnost izbora izračuna koliko maksimalno auto smije trošiti na 100km, ako je ciljana mjesečna potrošnja X eura?

def potrošnja_goriva ():
    kilometraza = budget/potrosnja_na100/cijena_benzina*100
    x = f'Sa ciljanom mjesečnom potrošnjom u iznosu od {budget} EUR uz cijenu goriva {cijena_benzina} po litri u EUR i sa potrošnjom na 100km: {potrosnja_na100}l možete prijeći {kilometraza} kilometara.'
    return x
budget = float(input('Unesite ciljanu mjesečnu potrošnju u eurima: '))
cijena_benzina = float(input('Unesite cijenu benzina: '))
potrosnja_na100 = float(input('Unesite potrošnju benzina u litrama na 100km: '))

print(potrošnja_goriva())