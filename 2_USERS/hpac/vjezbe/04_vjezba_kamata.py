štednja = float(input('Koliko imaš ušteđeno: '))
vrijeme_štednje = int(input('Koliko godina se štedi: '))
kamata = float(input('Kolika je kamata na štednju: '))

prinos = štednja*kamata*vrijeme_štednje

print(f'Prinos na štednju u {vrijeme_štednje}godina, na glavnicu {štednja}€ uz kamatu {kamata} iznosi {round(prinos,2)}€')