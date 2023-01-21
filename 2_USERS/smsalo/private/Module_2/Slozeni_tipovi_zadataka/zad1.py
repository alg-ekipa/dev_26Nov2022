#unos ocjena i prosjek ocjena svih učenika

zbroj_ocjena=[]
broj_ucenika=int(input("Upiši broj učenika u razredu "))
for i in range(broj_ucenika):
    ocjena=int(input("Unesi ocjenu učenika: "))
    zbroj_ocjena.append(ocjena)
prosjek=sum(zbroj_ocjena)/broj_ucenika
print(f"Prosjek ocjena {broj_ucenika} učenika u razredu iznosi {prosjek}")

print()

broj_petica=zbroj_ocjena.count(5)
print(f"Broj učenika koji imaju petice je {broj_petica}")

