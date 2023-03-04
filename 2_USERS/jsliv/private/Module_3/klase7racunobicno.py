#VARIJABLE
broj = "R1-202301"
datum = "4.03.2023."
stavke = {
    "Laptop": 12000,
    "Monitor": 2000,
    "Mis": 100,
    "Tipkovnica": 150
}

ukupno = 0
PDV = 0.25

for cijena in stavke.values():
    ukupno = ukupno + cijena
ukupno_pdv = ukupno*(1+PDV)

#Ispis racuna

print(broj)
print(datum)
print("------------------")
print("Proizvod\tCijena")
for proizvod, cijena in stavke.items():
    print(f"{proizvod}\t\t{cijena}")

print("-"*20)
print(f"UKUPNO:\t\t\t{ukupno_pdv}")
print(f"PDV:\t\t\t{ukupno*PDV}")

