stolovi_rjecnik = {
    '0186': ['stol Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['stol Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['stol Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['stol Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['stol Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['stol Lucas', 940.00, True, 'crna', 'drvo', 4]
}
for k, v in stolovi_rjecnik.items():
    sifra=k
    ime=v[0]
    cijena=v[1]
    stanje=v[2]
    boja=v[3]
    materijal=v[4]
    komada=v[5]
    
    try:
        with open('stolovi.txt', 'a') as file_writer:
            redak=f'{sifra}; {ime}; {cijena}; {stanje}; {boja}; {materijal}; {komada}\n'
            file_writer.write(redak)


    except Exception as e:
            print(f'Dogodila se pogreška {e}')