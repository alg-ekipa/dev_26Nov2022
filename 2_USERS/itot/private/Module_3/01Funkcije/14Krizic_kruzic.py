
'''
Odrađeno:
Crtanje igrace table
Provjera krivog unosa polja
nemogucnost ponovnog unosa na isto polje
projeva svih kombinacija gotove igre
nova igra
resetiranje table kod nove igre
brisanje ekrana
Izmjena prvog igraca kod gubitka partije
nerjeseno

TODO:
igra protiv CPU
Tablica rezultata na kraju igre
'''

import os
import random
mjesta_na_ploci=['O','1','2','3','4','5','6','7','8','9'] #prvo je O, a ne 0 radi kasnije provjere nereješenog

def ispis_ploce():
    
    print(f'''
    
        {mjesta_na_ploci[1]} | {mjesta_na_ploci[2]} | {mjesta_na_ploci[3]}
        --+---+--
        {mjesta_na_ploci[4]} | {mjesta_na_ploci[5]} | {mjesta_na_ploci[6]}
        --+---+--
        {mjesta_na_ploci[7]} | {mjesta_na_ploci[8]} | {mjesta_na_ploci[9]}
    
    ''')

def mjesto_upisa(igrac):
    na_koje_polje = input('Unesi zeljeno polje: ') 
    #provjera da li je broj i je li trazeni broj
    while na_koje_polje.isdigit() == False or int(na_koje_polje) not in [1,2,3,4,5,6,7,8,9] or mjesta_na_ploci[int(na_koje_polje)] in ['X','O']:  
        print('Pogrešan unos.')
        if na_koje_polje.isdigit() == False or int(na_koje_polje) not in [1,2,3,4,5,6,7,8,9]:
            print('Moraš upisati broj 1-9.\nUnesi zeljeno polje: ')
        #provjera jel vec upisano
        elif na_koje_polje.isdigit() == True and int(na_koje_polje) in [1,2,3,4,5,6,7,8,9] or mjesta_na_ploci[int(na_koje_polje)] in ['X','O']:
            print('Polje je vec popunjeno.\nUnesi zeljeno polje: ')

        na_koje_polje = input()
          
    #upis igracevog znaka na trazeno polje                       
    if igrac == 1:
        mjesta_na_ploci.pop(int(na_koje_polje))
        mjesta_na_ploci.insert(int(na_koje_polje),'X')
        return True
    if igrac == 2:
        mjesta_na_ploci.pop(int(na_koje_polje))
        mjesta_na_ploci.insert(int(na_koje_polje),'O')
        return True

def provjera_dobitnika():
    #print('Pocetak provjere dobitnika') #Test za izbrisati kasnije
    '''Vodoravna provjera'''
    if mjesta_na_ploci[1] == mjesta_na_ploci[2] == mjesta_na_ploci[3]:
        return mjesta_na_ploci[1]
    if mjesta_na_ploci[4] == mjesta_na_ploci[5] == mjesta_na_ploci[6]:
        return mjesta_na_ploci[4]
    if mjesta_na_ploci[7] == mjesta_na_ploci[8] == mjesta_na_ploci[9]:
        return mjesta_na_ploci[7]

    '''Okomita provjera'''
    if mjesta_na_ploci[1] == mjesta_na_ploci[4] == mjesta_na_ploci[7]:
        return mjesta_na_ploci[1]
    if mjesta_na_ploci[2] == mjesta_na_ploci[5] == mjesta_na_ploci[8]:
        return mjesta_na_ploci[2]
    if mjesta_na_ploci[3] == mjesta_na_ploci[6] == mjesta_na_ploci[9]:
        return mjesta_na_ploci[3]

    '''Kosa provjera'''
    if mjesta_na_ploci[1] == mjesta_na_ploci[5] == mjesta_na_ploci[9]:
        return mjesta_na_ploci[1]
    if mjesta_na_ploci[3] == mjesta_na_ploci[5] == mjesta_na_ploci[7]:
        return mjesta_na_ploci[3]

    '''Provjera jesu li sva polja popunjena'''
    nepopunjena_polja = 0
    for znak in mjesta_na_ploci:
        if znak not in ['X','O']:
            nepopunjena_polja += 1
    if nepopunjena_polja == 0 :
        return 'N' 

          
def nova_igra():
    odgovor = input('Zelis li novu igru? D/N ' )
    while odgovor.upper() not in ["D","N"]:
        odgovor = input('Pogrešan Unos! Zelis li novu igru? D/N ' )
    if odgovor.upper() == 'D':
        return 1
    if odgovor.upper() == 'N':
        return 0

#predefinicija igraca i igre
igra = 1
igrac = 1 

while igra == 1:
    
    while igrac == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\tIgrac {igrac} - X')
        ispis_ploce()
        mjesto_upisa(igrac)
        igrac = 2
        if provjera_dobitnika() != None:
            igrac = 0
         
    while igrac == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\tIgrac {igrac} - O')
        ispis_ploce()
        mjesto_upisa(igrac)
        igrac = 1
        if provjera_dobitnika() != None:
            igrac = 0

    if provjera_dobitnika() != None:
        os.system('cls' if os.name == 'nt' else 'clear')
        if provjera_dobitnika() == 'O':
            print(f'Igrac 2 - (O) je pobjedio')
            igrac = 1           #promjena igraca
        if provjera_dobitnika() == 'X':
            print(f'Igrac 1 - (X) je pobjedio')    
            igrac = 2           #promjena igraca
        if provjera_dobitnika() == 'N':
            print('Nerješeno!')
            igrac = random.randint(1,2)   #promjena igraca  
        ispis_ploce()
        povrat_nova_igra = nova_igra()
        if povrat_nova_igra == 1:
            mjesta_na_ploci=['0','1','2','3','4','5','6','7','8','9']
            
        
        elif povrat_nova_igra == 0:
            igra = 0

        

    
print('END While igra')             #Test za izbrisati kasnije