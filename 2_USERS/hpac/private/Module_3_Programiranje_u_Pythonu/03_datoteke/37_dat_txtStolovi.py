stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }


counter = 1

for k,v in stolovi_rjecnik.items():
    sifra = k
    ime = v[0]
    cijena = v[1]
    raspoloziv = v[2]
    dimenzija = v[3]
    boja = v[4]
    materijal = v[5]

    try:
        with open ('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/DrveniStolovi.txt','a', encoding='utf8') as file_writer:
            redak = f'{sifra};{ime};{cijena};{raspoloziv};{dimenzija};{boja};{materijal}\n'
            file_writer.write(redak)


    except Exception as e:
        print(f'Dogodila se pogreška {e}')


