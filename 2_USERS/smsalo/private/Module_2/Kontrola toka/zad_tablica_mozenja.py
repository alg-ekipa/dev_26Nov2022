# napraviti tablicu množenja. Korisnik unosi do kojeg broja se radi tablica

while True:
    broj=int(input('Unesi broj do kojeg zeliš tablicu množenja: '))
    for i in range (1,broj+1):
        for j in range (1,broj+1):
            print(i*j, end='\t')
        print()
    odluka=input('Zelite li unositi dalje? Za DA unesite 1, za NE unesite 0: ')
    if odluka=='0':
        break
