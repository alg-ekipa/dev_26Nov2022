stolovi_rjecnik = {
    '0186': ['stol Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['stol Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['stol Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['stol Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['stol Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['stol Lucas', 940.00, True, 'crna', 'drvo', 4]
}

for k, v in stolovi_rjecnik.items():
    sifra = k
    ime = v[0]
    cijena = v[1]
    raspoloziv = v[2]
    boja = v[3]
    materijal = v[4]
    komada = v[5]

    try:
        with open('D:/Vesna/dev_26Nov2022/dev_26Nov2022/1_ALG/_vzbo_/m3_03_datoteke/stolovi_rjecnik.txt','a') as file_writer:
            redak = f'{sifra};{ime};{cijena};{raspoloziv};{boja};{materijal};{komada}\n'
            file_writer.write(redak)

    except Exception as e:
        print(f'Pogreška: {e}')

# TO DO
# u datoteku ispisati podatke iz rječnika Svjetiljke i Tepisi