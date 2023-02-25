broj_kartice = input(max, 16 ("Unesite broj kartice: "))
sakriveni_broj_kartice = " "

print("Unesite znak kojim želite sakriti broj kartice: ")
znak = input()
duljina = len(broj_kartice)

i = 0

for slovo in broj_kartice:
    print(slovo, end= "")
    i = i + 1
    if i > (duljina -4):
        sakriveni_broj_kartice = sakriveni_broj_kartice + slovo
    elif slovo == " ":
        sakriveni_broj_kartice = sakriveni_broj_kartice + slovo
    else:
        sakriveni_broj_kartice = sakriveni_broj_kartice + znak

print()

print(f"Broj znamenka u broju kartice: \n {broj_kartice} je duljina {duljina}.")
print(f"Zakodirani broj kartice je: \n {sakriveni_broj_kartice}.")
