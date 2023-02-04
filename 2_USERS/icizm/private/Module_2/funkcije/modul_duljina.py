def duljina(): 
    print('Odaberi smijer konverzije: \n a. km u milje \n b. milje u km')
    odabir = input()


    if odabir == 'a': 
        km = float(input('Unesite udaljenost u kilometrima: '))
        milja = km * 0.62
        #return milja #nemamo lijepi ispis ako koristimo return
        print(f'{km} km = {milja} milja')

    if odabir == 'b': 
        m = float(input('Unesite udaljenost u miljama: '))
        kilom = m / 0.62
        #return kilom
        print(f'{m} milja = {kilom} km')