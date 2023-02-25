from modul_duljina import duljina # Smisao funkcije je da ju pozoveš iz drugog modula, da ne piše dugačko kod.

print(''' Odaberit tip konverzije:
        1. duljina
        2. temperatura
        3. masa
        4. volumen''')
odabir = int(input())

if odabir == 1:
    duljina()