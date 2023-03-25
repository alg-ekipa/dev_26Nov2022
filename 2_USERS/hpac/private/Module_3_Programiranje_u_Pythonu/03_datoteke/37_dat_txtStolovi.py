stolovi_rjecnik = {
    '0186' : ['stol Jack', 700.00, True, '120x90x80', 'smeđa', 'drvo'],
    '0203' : ['stol Kathy', 880.00, True, '130x90x80', 'smeđa', 'drvo'],
    '1234' : ['stol Tomy', 1250.00, True, '150x100x90', 'bijela', 'drvo'],
    '4002' : ['stol Ohm', 940.00, True, '120x90x80', 'crna', 'metal'],
    '0923' : ['stol Heda', 940.00, False, '120x90x80', 'crna', 'metal'],
    '1773' : ['stol Lucas', 940.00, True, '120x90x80', 'crna', 'drvo']
   }


counter = 1

for k,v in stolovi_rjecnik:
    if v[5] == 'drvo':
        try:
            file_writer = open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/DrveniStolovi.txt','a')
            redak = f'{stolovi_rjecnik.key}';{stolovi_rjecnik[0]};{stolovi_rjecnik[1]};{stolovi_rjecnik[2]};{stolovi_rjecnik[3]};{stolovi_rjecnik[4]};{stolovi_rjecnik[5]}'
            file_writer.write(stolovi_rjecnik)
            counter +=1

        except Exception as e:
            print(f'Dogodila se pogreška {e}')

        finally:
            file_writer.close()

