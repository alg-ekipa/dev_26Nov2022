poruka = 'Bok' # Gloablna varijabla

def pozdrav():
    global poruka #Global - trebao bi pozivati varijablu izvan funkcije, ali radi i bez toga
    ime = 'Lovro'
    #Poruka = 'Pozdrav'
    print(poruka)
    print(ime)

pozdrav()
print(poruka)
#print(ime) - NE RADI!!! zato što je ime lokalna varijabla

# Lokalne varijable - definirane i postoje samo unutar funkcije, glavni program je "ne vidi", u memoriji kratkog vijeka
# Globalne varijable - definiraju se izvan svih funkcija, prepozanju se u svim funkcijama, ostaju duže u memoriji