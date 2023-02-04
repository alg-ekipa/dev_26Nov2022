#izraditi funkciju za izračun površine jednakostraničnog trokuta, kasnije ih u glavnom programu ispišite 

import math

def racunaj_povrsina_jednakostranicnog_trokuta(a):
    #math.sqrt(x)
    P = a**2*math.sqrt(3)/4
    return P

def racunaj_visinu_jednakostranicnog_trokuta(a):
    V = a*math.sqrt(3)/2
    return V

a=float(input('Unesite duljinu stranice: '))

print(f'Povrsina jednakostraničnog trokuta iznosi {round(racunaj_povrsina_jednakostranicnog_trokuta(a),2)}cm2')
print()

print(f'Visina jednakostraničnog trokuta iznosi {round(racunaj_visinu_jednakostranicnog_trokuta(a),2)}cm')
print()