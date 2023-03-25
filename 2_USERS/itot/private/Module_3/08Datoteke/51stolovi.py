
file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/51stolovi_rijecnik.txt'

stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }



for x,y in stolovi_rjecnik.items():
    sifra = x
    redak = x+';' 
    lista_specifikacije = stolovi_rjecnik[x]   # ovo vec je lista, netreba pretvorba
    #print(lista_specifikacije)
    for z in lista_specifikacije:
        redak = redak + str(z) + ';'  # z je clan, ne treba indexirati
    redak = redak + '\n'
    file_weiter = open(file_path, "a")
    file_weiter.write(redak)
    



