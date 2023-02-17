'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću
vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:

• Stranice trokuta, površinu trokuta (P = (a*va)/2  , va je visina na stranicu a)
te opseg trokuta.
'''


stranica_a = int(input('Unesi stranicu a= '))
stranica_b = int(input('unesi stranicu b= '))
stranica_c = int(input('unesi stranicu c= '))

opseg = stranica_a + stranica_b + stranica_c

print(f"Opseg trokuta sa stranicama {stranica_a}, {stranica_b} i {stranica_c} je {opseg}")

# za P mi treba visina, visina