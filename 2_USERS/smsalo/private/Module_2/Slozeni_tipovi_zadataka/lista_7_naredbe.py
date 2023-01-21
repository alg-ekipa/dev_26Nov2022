ocjene_ucenika=[3, 2, 2, 4, 2, 5, 1, 5, 2, 4]
brojevi=[21, 33, 24, 54, 101, 4, 8, 12, 15, 1]
rijec="programiranje"
rijec_lista=list(rijec)

#print(f"Prije clear {brojevi}")
#brojevi.clear()
#print(f"Nakon clear {brojevi}")

ocjene_ucenika_kopija=ocjene_ucenika.copy()
print(ocjene_ucenika)
print(ocjene_ucenika_kopija)

broj_dvojki=ocjene_ucenika_kopija.count(2)
broj_petica=ocjene_ucenika_kopija.count(5)
print(f"Broj dvojki je {broj_dvojki}")
print(f"Broj petica je {broj_petica}")

print(rijec_lista)
r=rijec_lista.count("r")
print(f"Slovo r se pojavljuje {r}")

#na ocjene učenika dodajemo još a) jednu ocjenu i b)tri ocjene
print(ocjene_ucenika)
ocjene_ucenika.append(5)
print(f"Nakon append ocjene učenika je povećana za jedan član {ocjene_ucenika}")

nove_ocjene=[5,3,4]
ocjene_ucenika.extend(nove_ocjene)
print(f"Nakon extend: {ocjene_ucenika}")

print(brojevi)
print(brojevi.index(24))
brojevi.extend([24, 24])
print(brojevi.index(24))
print(brojevi)

brojevi.pop(3)
print(brojevi)

#sortiranje čanova liste 
# brojevi.reverse() trajno mijenja listu, naredba za varijablu je reversed()
print()
brojevi_obrnut=reversed(brojevi)
print(brojevi)
print(brojevi_obrnut)

#brojevi.sort() trajno mijenja listu, varijabli možemo pridružiti naredbu sorted()
brojevi_sortirano=sorted(brojevi)
print(brojevi)
print(brojevi_sortirano)

#kako složiti brojeve od najvećeg prema najmanjem
brojevi_sortirano.reverse()
print(brojevi_sortirano)

print(brojevi)
brojevi.insert(2,22)
print(brojevi)
brojevi.insert(7, "A")
print(brojevi)