import random
zamisljeni_broj=random.randint(1,100)
print(zamisljeni_broj)

igra=1
br_pokusaja=1

while igra:
    broj=input('Zamisljeni broj je između 1 i 100. Pokusajte pogoditi broj!')
    if broj.isdigit()==True and 0< int(broj) <101:
        while int(broj)!=zamisljeni_broj:
            br_pokusaja+=1
            if int(broj)>zamisljeni_broj:
                broj=int(input('Zamisljeni broj je manji od unesenog. Pokusajte ponovo!'))
            elif int(broj)<zamisljeni_broj:
                broj=int(input('Zamisljeni broj je veci od unesenog. Pokusajte ponovo!'))
        else:
            print(f'Bravo! Pogodili ste zamisljeni broj iz {br_pokusaja} pokusaja!')
        igra=int(input('Zelite li igrati ponovo? Za DA unesite 1, za NE unesite 0.'))
        if igra==0:
            break
        else:
            br_pokusaja=1
            zamisljeni_broj=random.randint(1,100)
    else:
        print('Unesite BROJ izmedu 1 i 100. ')





        