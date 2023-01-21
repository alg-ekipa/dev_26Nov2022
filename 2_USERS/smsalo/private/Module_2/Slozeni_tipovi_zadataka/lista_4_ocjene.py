ocjene_ucenika=[3, 2, 2, 4, 2, 5, 1, 5, 2, 4]
print(len(ocjene_ucenika))

zbroj=0
for ocjena in ocjene_ucenika:
    zbroj=zbroj+ocjena
prosjek=zbroj/len(ocjene_ucenika)
print(f"Prosjek ocjena je {prosjek}")

print()

print(sum(ocjene_ucenika))
print(zbroj)

