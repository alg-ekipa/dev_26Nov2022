from modul_predmeti import nadji_index as find

predmeti = ["Matematika", "Hrvatski", "Fizika", "Kemija", "Biologija"]

#Treba nam funkcija koja vrća indeks/redni broj određenog predmeta

#print(list(enumerate(predmeti)))   kako funkcionira enumerate

index = find(predmeti, "Fizika")
print("Redni broj predmeta u listi je: ", index+1)

