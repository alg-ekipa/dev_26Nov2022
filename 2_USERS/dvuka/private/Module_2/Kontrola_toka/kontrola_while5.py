#igra pogodi broj
import random

zamisljeni_broj=random.randint(1,100)
#print(zamisljeni_broj)


while 1:
    broj=input('Unesite broj u rasponu od 1 do 100: ')
    if int(broj)>=0 and int(broj)<=100:
        print('')
    else:
        print('Broj nije u zadanom raspnu, kušajte ponovno!')
    while broj.isdigit()==False:
        print('Krivi Unos! Morate unijeti Broj! Ponovite unos! ')
        broj=input('Unesi broj: ')
    if int(broj)==zamisljeni_broj:
        print('Pogodili ste broj')
        break
    elif int(broj)<zamisljeni_broj:
        print('Broj je manji od traženog! Pokušajte ponovno!')
    elif int(broj)>zamisljeni_broj:
        print('Broj je veći od traženog! Pokušajte ponovno!')

# To do
#unos stringa
#raspon bvrojeva
#nova igra
    