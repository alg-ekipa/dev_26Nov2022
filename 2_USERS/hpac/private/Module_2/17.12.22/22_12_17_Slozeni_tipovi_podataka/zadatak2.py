#napiši program koji unosi cijenu proizvoda, unsi broj proizvoda i njeiove cijene, koje se spremaju u liste. zatim ispiši najvišu i najnižu cijenu

lista_proizvoda = []
broj_proizvoda = int(input('Unesi broj proizvoda:'))

for i in range(broj_proizvoda):
    cijena_proizvoda = float(input(f'Unesi cijenu proizvoda {i+1}: '))
    lista_proizvoda.append(cijena_proizvoda)

najskuplji_proizvod = max(lista_proizvoda)
najjeftiniji_proizvod = min(lista_proizvoda)
razlika = najskuplji_proizvod - najjeftiniji_proizvod

print(f'Navjeća cijena proizvoda je {najskuplji_proizvod}, najniža cijena proizvoda je {najjeftiniji_proizvod}, a njihova razlika je {razlika}')

