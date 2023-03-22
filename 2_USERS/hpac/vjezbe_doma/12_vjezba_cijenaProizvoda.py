#napiši program koji unosi cijenu proizvoda, unsi broj proizvoda i njeiove cijene, koje se spremaju u liste. zatim ispiši najvišu i najnižu cijenu

lista_proizvoda = []
broj_proizvoda = int(input('Unesi broj proizvoda:'))

for i in range(broj_proizvoda):
    cijena = float(input(f'Unesi cijenu {i+1} proizvoda: '))
    lista_proizvoda.append(cijena)

max_cijena = max(lista_proizvoda)
min_cijena = min(lista_proizvoda)

razlika = max_cijena - min_cijena

print(f'Cijena najskupljeg proizvoda je {max_cijena}€, najjeftinijeg je {min_cijena}€, a njihova razlika je {round(razlika,2)}€')