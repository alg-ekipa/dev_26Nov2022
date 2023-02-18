poruka='Bok'

def pozdrav():
    global poruka
    ime='Lovro'
    poruka='Pozdrav'
    print(poruka)

pozdrav()

#Lokalne varijable-definirane i ostoje samo unutar funkcije, glavni program je ne vidi, u memoriji kratkog vijeka

#Gkobalne varijable-definiraju se izvan svih funkcija, preoznaju se u svim funkcijama, ostaju duže u memoriji