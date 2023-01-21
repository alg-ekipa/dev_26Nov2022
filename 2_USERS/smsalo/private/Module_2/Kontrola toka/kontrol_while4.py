# Unos broja u nekom rasponu, npr. između 10 i 20

#bez provjere unosi li korisnik broj ili string

while True:
    broj=int(input('Unesite broj u rasponu od 10 do 20! '))
    if broj>= 10 and broj <=20:
        print('Uspješan unos!')
        break
    else:
        print('Broj nije u zadanom rasponu, pokušajte ponovo! ')
print()

s='123'                     # funkicija .insdigit() provjerava da li su SVI u nizu brojevi
print(s.isdigit())

while True:
    broj_1=input('Unesite broj u rasponu od 10 do 20! ')
    while broj_1.isdigit() == False:
        print('Krivi unos! Morate unjeti broj! Pokušajte ponovo!')
        input('Unesite broj u rasponu od 10 do 20!')
    if int(broj_1) >=10 and int(broj_1) <= 20:
        print('Uspješan unos!')
        break
    else: print('Broj nije u rasponu od 10 do 20!')


password='tajno'
while True:
    unos=input('Unesi password: ')
    if unos==password:
        print('Točno!')
        break
    else:
        print('Krivi password! Pokušajte ponovo. ')
print()

