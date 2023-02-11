# program koji će za uneseni broj kartice sakriti sve znamenke osim zadnje 4

    
while True:
    br_kartice=input('Unesite br. kartice: ')
    if 5<len(br_kartice)<=16:
        znak=input('Unesite znak s kojim želite zaštititi broj kartice: ')
        break
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovo! ')
print()

brojevi=list(br_kartice)
#print(brojevi)

skrivena=[]
for i in range(0,len(br_kartice)-4):
    if brojevi[i]=='-':
        skrivena.append('-')
        i=i+1
    else:
        skrivena.append(znak)
#print(skrivena)

pod_lista=brojevi[-4:] 
#print(pod_lista)

br_skriveni=skrivena + pod_lista
#print(br_skriveni)

for broj in br_skriveni:
    print(broj, end='')



