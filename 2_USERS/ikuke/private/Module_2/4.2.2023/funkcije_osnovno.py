# funkcija koja vraća vrijednost (znakovni niz) i ima ulazni argument
def dohvati_pozdrav(ime):
    return f' Dobar dan, {ime}'

poruka = dohvati_pozdrav ('Igor')
print (poruka)
poruka_marko = dohvati_pozdrav ('Marko')

print (poruka_marko)