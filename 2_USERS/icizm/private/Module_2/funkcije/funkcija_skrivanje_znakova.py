'''broj kartice bolje da bude string jer kao integer nam ne znači ništa već nam treba kao niz. 
unosi se broj kao niz i onda se mijenja u prazan tekst pa zvijezdice len(prazan niz) slicanje itd
postaviti uvijet fiksno 16 ili postaviti nesmije biti manje od 5 

''' 


def skrivanje_znakova(broj_kartice): 
    skriveni_broj = ''
    simbol = '#'
    
    input('Unesite broj kartice: ')
