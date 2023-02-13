import os
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

TODO:
nerjeseno
CPU - rnd
Tablica rezultata




'''
mjesta_na_ploci=['0','1','2','3','4','5','6','7','8','9']

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
            print('Mora biti broj 1-9.\nUnesi zeljeno polje: ')
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
          
def nova_igra():
    #print('Pocetak nova_igra')  #Test za izbrisati kasnije
    odgovor = input('Zelis li novu igru? D/N ' )
    #print(f'odgovor prije WEHILE {odgovor}') #Test za izbrisati kasnije
    while odgovor.upper() not in ["D","N"]:
        #print(f'odgovor WEHILE1 {odgovor}') #Test za izbrisati kasnije
        odgovor = input('Pogrešan Unos! Zelis li novu igru? D/N ' )
        #print(f'odgovor WEHILE2 {odgovor}') #Test za izbrisati kasnije
    if odgovor.upper() == 'D':
        return 1
    if odgovor.upper() == 'N':
        return 0

igra= 1
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
            sljedeci_igrac = 1
        if provjera_dobitnika() == 'X':
            print(f'Igrac 1 - (X) je pobjedio')    
            sljedeci_igrac = 2            
        ispis_ploce()
        povrat_nova_igra = nova_igra()
        if povrat_nova_igra == 1:
            mjesta_na_ploci=['0','1','2','3','4','5','6','7','8','9']
            #promjena igraca
            igrac = sljedeci_igrac 
        elif povrat_nova_igra == 0:
            igra = 0

        

    
print('END While igra')             #Test za izbrisati kasnije