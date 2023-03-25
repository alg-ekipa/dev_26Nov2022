

stolovi_rjecnik = {
    '0186': ['Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['Lucas', 940.00, True, 'crna', 'drvo', 4]
}


for k,v in stolovi_rjecnik.items():
    key = k 
    name = v[0]
    price = v[1]
    available = v[2]
    color = v[3]
    material = v[4]
    pieces = v[5]
        
    
    try:
        with open("stolovi.txt", 'a') as file_writer:
            line = f'{key};{name};{price};{available};{color};{material};{pieces}\n' 
            file_writer.write(line) 

    except Exception as e:
        print(f'Error message: {e}')

    finally:
        file_writer.close()
