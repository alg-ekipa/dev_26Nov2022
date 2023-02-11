'''broj kartice bolje da bude string jer kao integer nam ne znači ništa već nam treba kao niz. 
unosi se broj kao niz i onda se mijenja u prazan tekst pa zvijezdice len(prazan niz) slicanje itd
postaviti uvijet fiksno 16 ili postaviti nesmije biti manje od 5 
ikuke - riješio kao unos riječi kad smo imali
s

''' 


dbroja = len(broj_kartice)
skriveni_broj = ''
simbol = '#'
    
while True:
    broj_kartice = input('Unesite broj kartice: ')
    if dbroja < 16: 
        print('Niste unijeli potpuni broj kartice. Pokušatje ponovno.')
    else:
        print('Hvala')

'''
def skrivanje_znakova(broj_kartice): 
    dbroja = len(broj_kartice)
    skriveni_broj = ''
    simbol = '#'
    
    if dbroja < 16: 
        print('Niste unijeli potpuni broj kartice. Pokušatje ponovno.')
    else:
       
    

skrivanje_znakova(broj_kartice)'''