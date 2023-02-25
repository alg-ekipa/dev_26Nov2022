def povecaj(broj, za_koliko=5):
    '''Funkcija koja povećava broj za neki iznos'''
    return broj + za_koliko

print(povecaj.__doc__) #ispis teksta iz doc stringa
print(povecaj.__name__) #ispis imena funkcije
print(povecaj(18))
print()
