poruka = 'Bok'  # poruka je globalna varijabla

def pozdrav(ime):
    global poruka
    ime = 'Lovro'
    #poruka = 'Pozdrav'
    print(poruka)
    print(ime)  # ime je lokalna varijabla

pozdrav('Ivan')
print(poruka)
#print(ime) -- ne radi!!

# Lokalne varijable - definirane i postoje samo unutar funkcije, glavni program je "ne vidi", u memoriji kratkog vijeka
# Globalne varijable - definiraju se izvan svih funkcija, prepoznaju se u svim funkcijama, ostaju duže u memoriji