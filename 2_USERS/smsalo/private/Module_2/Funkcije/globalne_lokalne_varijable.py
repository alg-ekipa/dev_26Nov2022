poruka='Bok'

def pozdrav(ime):
    print(poruka)
    print(ime) #ime je lokalna varijabla i glavni program ju ne vidi/raspoznaje


pozdrav('Ivan')
print(ime)   #ne može jer je lokalna varijabla

# lokalne varijable - definirane i postoje samo unutar funkcije, glavni program ju ne vidi, u memoriji kratkog vijeka
# globalne varijable - definiraju se izvan svih funkcija, prepoznaju se u svim funkcijama, ostaju duže u memoriji

