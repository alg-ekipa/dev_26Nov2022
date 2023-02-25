#napraviti zablicu mnozenja, korisnik unosi do kojeg broja
'''
for i in range(1,11):
    for j in range(1,11):
        print (i*j, end='\t')
    print()
'''

os_x = int(input('Koliko brojeva će biti na x koordinati: '))
os_y = int(input('Koliko brojeva će biti na y koordinati: '))

for i in range(1, os_y+1):
    for j in range(1,os_x+1):
        print (i*j, end='\t')
    print()
