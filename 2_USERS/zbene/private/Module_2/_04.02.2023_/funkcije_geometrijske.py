#import math as m
from math import pi, pow, sqrt #from math import * povlači sve iz math ali zbog memorije procesora itd nepotrebno

#korištenje konstante pi iz math
def racunaj_povrsinu_kruga (r):
    P = r**2*pi
    return P

povrsina_kruga = racunaj_povrsinu_kruga(4)

print (f'Površina kruga iznosi {povrsina_kruga} cm2')
print()

#korištenje i funkcije pwer iz math
def racunaj_povrsinu_kruga(r):
    return pow(r,2)*pi

P = racunaj_povrsinu_kruga(4)

print (P)
print()

#Izraditi funkciju za izračun površine i visine jednakostraničnog trokuta, kasnije ih u glavnom programu ispišite
def racunaj_povrsinu_trokuta (a):
    return a**2*sqrt(3)/4

def racunaj_visinu_a (a):
    return a*sqrt(3)/2

K = racunaj_povrsinu_trokuta (5)
V = racunaj_visinu_a (5)

print(f'Površina jednakostraničnog trokuta iznosi {K}cm2 a visina jednakostraničnog trokuta iznosi {V}cm')    
