#Izračun mjesečne potrošnje el. struje te cijene el. struje koju potroši mikrovalna pećnica snage 1,3kW ako se koristi 2 sata dnevno? Uzmimo da je cijena 1kWh jednaka 1kn.

mikrovalna_pecnica = float(input('Unesi potrošnju pećnice: '))
dnevno = int(input('Unesi koliko se sati dnevno koristi pećnica: '))
kWh = int(input('Unesi kolika je cijena 1kWh u kunama'))
mjesec = int(input('Unesi broj dana u mjesecu: '))

Izračun = mikrovalna_pecnica*dnevno*kWh*mjesec
print('Mjesečna potrošnja iznosi:',Izračun, 'kn')