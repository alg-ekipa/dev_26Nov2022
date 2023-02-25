ocjene_ucenika = [3,2,4,4,3,5,5,2,1,3]
#print(len(ocjene_ucenika))

zbroj=0
for ocjena in ocjene_ucenika:
    #print(ocjena)
    zbroj = zbroj + ocjena
prosjek = zbroj/len(ocjene_ucenika)

print(f'Prosjecna ocjena je {prosjek}')


print()
print(sum(ocjene_ucenika))
print(zbroj)