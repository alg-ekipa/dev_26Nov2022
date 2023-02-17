'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću
vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:
• Ime, prezime, godinu rođenja, državu rođenja, status radnog odnosa,
težinu te spol
• Stranice a i b, četverokuta te za površinu tog četverokuta.
'''



ime = 'Petar'
prezime = 'peric'
godina_rodena = 1995
drzava_rodjena = 'Hrvatska'
zaposlen = True
masa = 86.7
spol = 'M'

print('Zovem se', ime, prezime)
print('zovem se', ime, prezime, sep='') # razmmak kod zarezaa je '' umjesto ' '

stranica_a = 5
stranica_b = 12
povrsina_pravokutnika = stranica_a*stranica_b

print(f"povrsina pravokutnika je {povrsina_pravokutnika}")