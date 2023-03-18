from modul_predmeti import nađi_indeks as find


predmeti = ['matematika', 'hrvatski', 'fizika', 'kemija', 'biologija']

#treba nam funkcija koja vraća indeks/redni broj određenog predmeta

#print (list(enumerate(predmeti))) --> kako funkcionira enumerate

index = find (predmeti,'fizika')
print ('Redni broj predmeta u listi je:', index+1)