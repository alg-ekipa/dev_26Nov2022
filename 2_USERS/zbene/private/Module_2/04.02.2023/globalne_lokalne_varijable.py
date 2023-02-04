poruka = 'Bok' #ovo je globalna varijabla

def pozdrav():
    global poruka
    ime = 'Lovro'
    #poruka = 'Pozdrav'
    print (poruka)
    print (ime) #ime je lokalna varijabla

pozdrav('Ivan')
print(poruka)
#print(ime) #- ovo ne radi

#lokalne varijable - definirane i postoje samo unutar funkcije, glavni program je "ne vidi", u memoriji kratkog vijeka
#globalne varijable - definiraju se izvan svih funkcija, prepoznaju se u svim funkcijama, ostaju duže u memoriji