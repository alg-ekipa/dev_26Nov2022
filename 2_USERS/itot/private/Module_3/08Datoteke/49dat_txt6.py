# citanje i formatiranje procitanog fila


try: 
    with open('C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/47adresar.txt') as file_reader:
        #file_data = file_reader.read()
        #print(file_data)
        #print(type(file_data))
        for red in file_reader:
            djelovi_retka = red.split(';')
            print(djelovi_retka)
            redni_broj = djelovi_retka[0]
            ime = djelovi_retka[1]
            prezime = djelovi_retka[2]
            mob = djelovi_retka[3].rstrip()
            print(redni_broj, ime, prezime, mob )

except Exception as e:
    print (f'Pogreska: {e}')







