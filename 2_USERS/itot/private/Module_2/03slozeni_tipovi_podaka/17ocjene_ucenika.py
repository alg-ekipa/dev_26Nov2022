'''
Unesi ocjene nekokga ucenika i izracunaj njegovu aritmeticku sredinu

'''



ocjene_ucenika = [1,5,2,3,1,2,3,5,2,1,2,3,2,1,5,]
print(len(ocjene_ucenika))
zbroj_ocjena=0

for ocjena in ocjene_ucenika:
    zbroj_ocjena += ocjena

prosjek_ocjena = zbroj_ocjena / len(ocjene_ucenika)
print(f'{zbroj_ocjena} / {len(ocjene_ucenika)} = {prosjek_ocjena}')
print(f'Prosjek ocjena ucenika je {zbroj_ocjena / len(ocjene_ucenika)}')


'''Opcija sum'''
print(sum(ocjene_ucenika))