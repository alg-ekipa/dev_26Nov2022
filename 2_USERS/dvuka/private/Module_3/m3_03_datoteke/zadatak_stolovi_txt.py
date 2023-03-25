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
    sifra=k
    ime=v[0]
    cijena=v[1]
    raspolozivost=v[2]
    boja=v[3]
    materijal=v[4]
    komada=v[5]

    try: 
        with open('C:/Users/grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/m3_03_datoteke/stolovi.txt', 'a') as file_writer:
             redak = f'{sifra};{ime};{cijena};{raspolozivost};{boja};{materijal};{komada}\n'
             file_writer.write(redak)

    except Exception as e: 
        print('Dogodila se pogreška {e}')

 


  

   