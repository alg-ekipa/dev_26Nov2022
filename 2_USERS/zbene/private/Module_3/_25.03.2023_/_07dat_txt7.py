stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
}

for k,v in stolovi_rjecnik.items():
    šifra = k
    ime = v[0]
    cijena = [1]
    raspoloživost = v[2]
    boja = v[3]
    materijal = v[4]
    stanje = v[5]

    try:
        with open('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/stolovi_rjecnik.txt', 'a', encoding='utf8') as file_writer:
            redak = f'{šifra} {ime} {materijal}\n'
            file_writer.write(redak)
        
    except Exception as ex:
        print (f'dogodila se pogreška {ex}')