potrosnja_mikrovalna =  float(input('unesi potrošnju potrošača u KW = '))
vrijeme_koristenja = float(input('unesi dnevno vijreme korištenja potrosaca u satima = '))
cijena_kw = float(input('cijenu kw = '))

broj_dana = int(input("koliko mjesec ima dana? ") )

mjesecna_potrosnja = broj_dana * vrijeme_koristenja * potrosnja_mikrovalna * cijena_kw

print(f'Mjesecna potrosnja za {broj_dana} dan/a je {mjesecna_potrosnja} kn')