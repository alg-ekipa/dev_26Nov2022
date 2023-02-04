#import math as m
from math import pi, pow

# korištenje konstante pi iz math
def racunaj_povrsinu_kruga(r):
    P = r**2*pi
    return P

povrsina_kruga = racunaj_povrsinu_kruga(4)

print(f'Povrsina kruga iznosi {round(povrsina_kruga,2)} cm2')

# korištenje i funkcije power iz math
def racunaj_povrsinu_kruga(r):
    return pow(r,2)*pi

P = racunaj_povrsinu_kruga(4)

print(P)


# Izraditi funkcije za izračun površine i visine jednakostraničnog trokuta, kasnije ih u glavnog programu ispišite 