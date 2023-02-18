#kreiraj varijable Izračun mj. potrošnje el struje te cijene el. struje koju potroši mikrovalna pećnica snage 1,3 kW ako se koristi 2 sata dnevno 1 kWh je 1 kn
snaga_pecnice = float(input('Unesi snagu pećnice:'))
dnevna_potrosnja = int(input('Unesi koliko sati dnevno se koristi pećnica:'))
dana_u_mjesecu = int(input('Unesi koliko se dana mjesečno koristi pećnica:'))

mjesecna_potrosnja = snaga_pecnice * dnevna_potrosnja * dana_u_mjesecu

print ('Mjesečna potrošnja električne struje mikrovalne pećnice iznosi:', mjesecna_potrosnja, 'kn')
