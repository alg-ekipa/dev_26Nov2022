#napraviti da korisnik unese veličinu tablice
while True: 
    broj = int(input('Unesite broj za veličinu svoje tablice množenja: '))
    for i in range(1,broj+1): 
        for j in range(1,broj+1):
            print(i*j, end = '\t')
        print()
        
    odluka = input('Želite li kreirati drugu tablicu? da / ne ')
    if odluka == 'ne':
        break