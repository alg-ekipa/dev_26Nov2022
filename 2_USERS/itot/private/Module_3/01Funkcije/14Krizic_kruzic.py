


mjesta_na_ploci=['0','1','2','3','4','5','6','7','8','9']
igra=1

def ispis_ploce():
    print(mjesta_na_ploci[1], mjesta_na_ploci[2], mjesta_na_ploci[3])
    print(mjesta_na_ploci[4], mjesta_na_ploci[5], mjesta_na_ploci[6])
    print(mjesta_na_ploci[7], mjesta_na_ploci[8], mjesta_na_ploci[9])

def mjesto_upisa(igrac):
    na_koje_polje = input('Unesi zeljeno polje: ') 
    #provjera da li je broj i je li trazeni broj
    while na_koje_polje.isdigit() == False or int(na_koje_polje) not in [1,2,3,4,5,6,7,8,9]:  
        na_koje_polje = input('Pogrešan unos, polje. Mora biti broj 1-9.\nUnesi zeljeno polje: ')       
    #provjera jel vec upisano
    while na_koje_polje.isdigit() == False or mjesta_na_ploci[int(na_koje_polje)] in ['X','O']:                                    
            na_koje_polje = input('Pogrešan unos, polje je vec popunjeno.\nUnesi zeljeno polje: ') 
    #upis igracevog znaka na trazeno polje                       
    if igrac == 1:
        mjesta_na_ploci.pop(int(na_koje_polje))
        mjesta_na_ploci.insert(int(na_koje_polje),'X')
    if igrac == 2:
        mjesta_na_ploci.pop(int(na_koje_polje))
        mjesta_na_ploci.insert(int(na_koje_polje),'O')

def provjera_dobitnika():
    
    if mjesta_na_ploci[1] == mjesta_na_ploci[2] == mjesta_na_ploci[3]:
        if mjesta_na_ploci[1] == 'O':
            return 1
        if mjesta_na_ploci[1] == 'X':
            return 2

igrac = 1 
while igra == 1:
    while igrac == 1:
        print(f'Igrac {igrac} - O')
        ispis_ploce()
        mjesto_upisa(igrac)
        igrac = 2
        print('END While igrac 1')  #Test za izbrisati kasnije
        provjera_dobitnika()
        if provjera_dobitnika() in [0,1,2]:
            print(f'Igrac {igrac} je pobjedio')
    while igrac == 2:
        print(f'Igrac {igrac} - X')
        ispis_ploce()
        mjesto_upisa(igrac)
        igrac = 1
        print('END While igrac 2')  #Test za izbrisati kasnije

    print(provjera_dobitnika())
    
print('END While igra')             #Test za izbrisati kasnije
    










ispis_ploce()