# Izraditi funkcije za izračun površine i visine jednakostranićnnog trokuta, kasnije ih u glavnom programu ispišite

from math import pow, sqrt

def racunaj_povrsinu_trokuta (a):
    return pow(a,2)*sqrt(3)/4

def racunaj_visinu(a):
    return a*sqrt(3)/2

a = float(input('Kolika je stranica trokuta: '))

P = racunaj_povrsinu_trokuta(a)
v = racunaj_visinu(a)

print(f'Povrišina trokuta je {round(P,2)} cm2, a njegova visina je {round(v,2)}')
