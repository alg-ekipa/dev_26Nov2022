poruka = 'Bok'

def pozdrav(): 
    global poruka #povuče varijablu iz glavog programa da bi ju vidjela funkcija
    ime = 'Lovro'
    #poruka = 'Pozdrav'
    print(poruka)
    print(ime) # ime je lokalna varijabla 

pozdrav('Ivan')
print(poruka)
print(ime)

# Lokalne varijable - definirane i postoje samo unutar funkcije, glavni program je ne vidi - koriste se samo dok se pozove funcija i to je to, one su KRATKOTRAJNE
# Globalne varijable - definiraju se izvan svih funkcija i prepoznaju se u svim funkcijama - ostaju DUŽE u memoriji


