# unos broja u nekom rasponu, npr. između 10 i 20
'''
while True: 
    broj = int(input('Unesite broj u rasponu od 10 do 20!'))
    if broj >= 10 and broj <= 20:
        print('Uspješan unos!')
        break
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovno!')
        
'''
#s = '123asd' 
#print(s.isdigit()) #vraća True ako su u nizu samo brojevi, ako nisu, vraća FALSE


while True: 
    unos = input('Unesite broj u rasponu od 10 do 20!')

    while unos.isdigit() == False:
        print('Krivi unos, morate unijeti broj! Ponovite unos!')
    unos = input('Unesite broj u rasponu od 10 do 20!')
    if int(unos) >= 10 and int(unos) <= 20: 
        print('uspješan unos!')
        break

    else: 
        print('Broj nije u zadanom rasponu. Pokušajte ponovno!')
