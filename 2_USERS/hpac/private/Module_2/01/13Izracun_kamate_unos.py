'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću
vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:
• Imate 10000 kn i možete zaboraviti na njih na 15 godina. Ako Vam
banka nudi 2.5% godišnju kamatu za taj iznos, koliko ćete zaraditi
nakon 15 godina. Jednostavni kamatni račun k = C * p * t
• k = iznos kamata odnosno prinos
• C = iznos glavnice
• p = godišnja kamatna stopa – NAPOMENA: 5% = 5 / 100 = 0.05
• t = vrijeme u godinama

Dodatak:
... tako da za unos vrijednosti pitate korisnika
'''

print("Decimalna mjesta moraju biti odvojena točkom '''.''!")
Iznos_glavnice = float(input("Unesite iznos glavnice: "))
godisnja_kamatna_stopa = float(input("Unesite godišnju kamatu: "))
vrijeme_u_godinama = float(input("Unesite period štednje u godinama: "))

iznos_kamate = Iznos_glavnice*godisnja_kamatna_stopa*vrijeme_u_godinama
print(f'Kamata za {vrijeme_u_godinama} godina je {iznos_kamate} kn.')