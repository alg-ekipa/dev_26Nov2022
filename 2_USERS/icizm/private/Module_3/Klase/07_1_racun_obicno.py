#VARIJABLE
broj = 'R1-2023-01'
datum = '04.03.2023.'
stavke = {
    'Laptop' : 12000, 
    'Monitor' : 2000, 
    'Miš' : 100, 
    'Tipkovnica' : 150
}

ukupno = 0
PDV = 0.25

# IZRAČUN IZNOSA RAČUNA

for cijena in stavke.values(): 
    ukupno = ukupno + cijena 

ukupno_PDV = ukupno*(1+PDV)

# IZRAČUN PDV-a

pdv_od_racuna = ukupno * PDV 

# ISPIS RAČUNA

print(broj)
print(datum)
print('*'*40)
print('Proizvod \t\t Cijena')
for proizvod,cijena in stavke.items():
    print(f'{proizvod}\t\t{cijena}')
print('-'*40)
print(f'Ukupno: \t\t\t{ukupno_PDV}')
print(f'PDV: \t\t\t\t{pdv_od_racuna}')