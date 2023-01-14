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
'''

Iznos_glavnice = 10000
godisnja_kamatna_stopa = 0.025
vrijeme_u_godinama = 15

iznos_kamate = Iznos_glavnice*godisnja_kamatna_stopa*vrijeme_u_godinama
print(f'Kamata za {vrijeme_u_godinama} godina je {iznos_kamate} kn.')