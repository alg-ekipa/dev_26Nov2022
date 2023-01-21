#unosi cijene određenog broja proizvoda sa cijenama 
# te se ispisuje najviša i najniža cijena te njihova razlika

cijena_proizvoda=[]
broj_proizvoda=int(input("Upiši broj proizvoda "))
for i in range(broj_proizvoda):
    cijena=float(input("Unesi cijenu proizvoda: "))
    cijena_proizvoda.append(cijena)
najveca=max(cijena_proizvoda)
najmanja=min(cijena_proizvoda)
razlika=najveca-najmanja
print(f"Najmanja cijena je {najmanja}, najveća cijena je {najveca}, a njihova razlika je {razlika}.")
