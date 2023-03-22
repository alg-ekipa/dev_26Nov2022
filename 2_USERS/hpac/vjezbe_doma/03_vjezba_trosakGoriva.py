potrošnja = float(input('Koliko goriva troši automobil: '))
cijena_goriva = float(input('Koliko košta litra goriva: '))
udaljenost = float(input('Koliko ima km do posla: '))
dani = int(input('Koliko radnih dana u mjesecu: '))

cijena_km = potrošnja*cijena_goriva/100
trošak_do_posla = cijena_km*udaljenost*dani

print(f'Mjesečni trošak automobila za vožnju do posla je {round(trošak_do_posla,2)}€, a po km je {round(cijena_km,2)}€')