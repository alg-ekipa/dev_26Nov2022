'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću
vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:

• Izračun mjesečne potrošnje el. struje te cijene el. struje koju potroši
mikrovalna pećnica snage 1,3 kW ako se koristi 2 sata dnevno?
'''

potrosnja_mikrovalna = 1.3
vrijeme_koristenja = 2
cijena_kw = 1

broj_dana = int(input("koliko mjesec ima dana? ") )

mjesecna_potrosnja = broj_dana * vrijeme_koristenja * potrosnja_mikrovalna * cijena_kw

print(f' mmjesecna potrosnja za {broj_dana} dan/a je {mjesecna_potrosnja} kn')