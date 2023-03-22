#Zadatak mjesečna potrošnja struje

dani = int(input('Koliko ima dana u mjesecu: '))
snaga = 1.3
vrijeme = float(input('Koliko sati dnevno se koristi: '))
cijena = 1



trošak = dani*snaga*vrijeme*cijena

print(f'Mjesečni trošak mikrovalne pećnice je {trošak}kn')
