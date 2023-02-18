def duljina():
    print('Odaberite smjer konverzije:\n a.km u milje\nb.milje u km')
    odabir=input()

    if odabir=='a':
        km=float(input('Unesite udaljenost u km:'))
        milja=km*0.62
        #return milja
        print(f'{km} km= {milja} milja')

    if odabir=='b':
        m=float(input('Unesite udaljenost u mljama;'))
        kilom=m/0.62
        #return kilom
        print(f'{m} milja {kilom} km')

print('''Odaberite tip konverzije:
        1.duljina
        2.temperatura
        3.masa
        4.volumen''')
odabir=int(input())

if odabir==1:
    duljina()


