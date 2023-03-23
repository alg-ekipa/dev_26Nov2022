# Izraditi funkcije za izračun površine i visine jednakostranićnnog trokuta, kasnije ih u glavnom programu ispišf

from math import pow, sqrt

def pov_trokuta(a):
    P = pow(a,2)*sqrt(3)/4
    return P

def visina_trokuta (a):
    va = a*sqrt(3)/2
    return va

a = int(input('Stranica trokuta: '))

povrsina = pov_trokuta(a)
visina = visina_trokuta(a)

print(f'Površina trokuta je {round(povrsina,2)}, strnica a={a}, a visina je {round(visina,2)}')
print()

# dodatno

def povecaj(broj, za_koliko = 5):
    '''Funkcija koja povećava broj za neki iznos'''
    return broj+za_koliko

print(povecaj.__doc__) #ispis teksta iz doc stringa
print(povecaj.__name__) #ispis imena funkcije
print(povecaj(18,3))
print()