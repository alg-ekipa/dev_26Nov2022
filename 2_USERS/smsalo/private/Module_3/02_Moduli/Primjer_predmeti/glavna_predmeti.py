
from modul_predmeti import nadi_index

predmeti=['matematka', 'hrvatski', 'fizika', 'kemija', 'biologija']

#treba nam funkcija koja vraća index/redni broj određenog predmeta
#print(list(enumerate(predmeti)))   kako funkcionira enumerate

index= nadi_index(predmeti, 'fizika')
print('Redni broj predmeta u listi je: ', index+1)




