def duljina():
    print('Odaberite smjer konverzije:\na. km u milje\nb. milje u km')
    odabir = input()

    if odabir == 'a':
        km = float(input('Unesite udaljenost u km: '))
        milja = km * 0.62
        #return milja
        print(f'{km} km = {milja} milja')

    if odabir == 'b':
        m  = float(input('Unesite udaljenost u miljama: '))
        kilom = m / 0.62
        #return kilom
        print(f'{m} milja = {kilom} km')