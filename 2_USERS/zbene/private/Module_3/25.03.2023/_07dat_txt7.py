stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
}

counter = 1

while stol in stolovi_rjecnik:
    for k,v in stolovi_rjecnik:
           materijal = v[6]

    if materijal == 'drvo':
        print()

    try:
        file_writer = open('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/adresar3.txt', 'a')
        redak = f'{counter};{v[6]}\n'
        file_writer.write(redak)
        counter +=1

    for red in file_reader:
            dijelovi_retka = red.split(';')
            #print (dijelovi_retka)
            redni_broj = dijelovi_retka [0]
            ime = dijelovi_retka [1]
            prezime = dijelovi_retka [2]
            mob = dijelovi_retka [3].rstrip
            
            contacts_object = Contact (redni_broj, ime, prezime, mob)
            contacts_object.print_contact()


    except Exception as e:
        print (f'dogodila se pogreška {e}')

    finally:
        file_writer.close()