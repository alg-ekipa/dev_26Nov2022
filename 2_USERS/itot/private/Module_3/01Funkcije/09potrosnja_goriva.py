


cijena_goriva = input('Unesi cijenu goriva u Eurima: ')
napravljeni_kilometri = input('Unesi napravljene kilometre: ')
utočeno_gorivo = input('Unesi količinu utočenog ogriva u Litrama: ')


potrosnja_lit =int(napravljeni_kilometri) / int(utočeno_gorivo)  
potrosnja_eur = potrosnja_lit * int(cijena_goriva)
print(f' Potrosnja goriva je {potrosnja_lit} litara, odnosno {potrosnja_eur} €')

