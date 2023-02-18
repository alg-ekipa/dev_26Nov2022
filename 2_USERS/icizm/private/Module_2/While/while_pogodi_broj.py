#igra pogodi broj
import random 

pogodi = random.randint(1, 100)

while 1:
    broj = int(input('Unesi broj! '))
    if broj == pogodi: 
        print('Pogodili ste broj!')
        break
    elif broj==0:
        break
    elif broj < pogodi: 
        print('Broj je veći! Pokušajte ponovno!')
    elif broj > pogodi: 
        print('Broj je manji! Pokušajte ponovno!')
    
'''
To do: 
unos stringa
raspon brojeva
nova igra?
'''