""" Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:
• Ako automobil troši 5.3 litara na 100 km i ako je cijena goriva 9.56 kn po litri (nije važno kojeg goriva).
Izračunajte koliko košta 1 km vožnje automobilom.
Prikažite mjesečni trošak (30 dana) odlaska na posao automobilom koji je udaljen 20 km u jednom smjeru. """

fuel_price = 9.53
car_consumption = 5.3
avg_daily_km = 40
avg_daily_per_month = 30

fuel_price_per_km = round((fuel_price * car_consumption) / 100,3)
print(f'You car consumption per kilometer is ~{fuel_price_per_km}HRK')

fuel_cost_per_month = (avg_daily_km * fuel_price_per_km ) * avg_daily_per_month 
print(f'Total cost of fuel per month: {fuel_cost_per_month}HRK')
# Ovo ti ne valja.



