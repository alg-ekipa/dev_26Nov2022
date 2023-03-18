from modul_predmeti import nadji_indeks


predmeti = ['matematika', 'hrvatski', 'fizika', 'kemija', 'biologija']

# treba nam funkcija koja vraća indeks/redni broj određenog predmeta

# print(list(enumerate(predmeti))) - kako funkcionira enumerate

indeks = nadji_indeks(predmeti, 'fizika')
print('Redni broj predmeta u listi je:', indeks+1)