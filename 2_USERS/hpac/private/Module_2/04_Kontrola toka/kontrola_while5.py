#IGRA POGODI BROJ, 

import random
zamisljeni_broj = random.randint(1,100)
#print(zamisljeni_broj)

'''
while 1: #True ili 1 je ista funkcija 
    broj = input('Unesi broj u rasponu od 1 do 100: ')
    while broj.isdigit() == False:
        print('UNESI BROJ, ne slova. čitaj malo bolje!!!!')
        broj = input('Unesi broj u rasponu od 1 do 100: ')
    if int(broj) == zamisljeni_broj:
        print('POGODAK!!! ')
        break
    elif int(broj)  < zamisljeni_broj:
        print('Broj je manji od zadanog, pokušajte ponovno!!')
    elif int(broj)  > zamisljeni_broj:
        print('Broj je veći od zadanog, pokušajte ponovno!!')
'''

#TO DO:
# - unos stringa
# - raspon brojeva
# - nova igra

while True: 
    broj = input('Unesi broj između 1-100: ')
    while broj.isdigit() == False:
        print('UNESI BROJ, ne slova. čitaj malo bolje!!!!')
        broj = input('Unesi broj u rasponu od 1 do 100: ')
    if 1<=int(broj)<=100:
        if int(broj)<zamisljeni_broj:
            print('Unešeni broj je manji od traženog')
        elif int(broj)>zamisljeni_broj:
            print('Unešeni broj je veći od traženog')
        elif int(broj)==zamisljeni_broj:
            print('BINGO!!')
            break
    else:
        print('Unešeni broj niju unutar traženog raspona')

    

