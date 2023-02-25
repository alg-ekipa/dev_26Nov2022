import os

polje_br=[0,1,2,3,4,5,6,7,8,9]

def crtanje_ploce():
    os.system('cls'if os.name=='nt' else 'clear')   #brise ekran

    print('\n\t Križić - kružić\n')

    print('\t Igrač 1 je križić: X \n\t Igrač 2 je kružić: O \n')

    print('\t\t   |   |   ')
    print(f'\t\t {polje_br[1]} | {polje_br[2]} | {polje_br[3]} ')
    print('\t\t___|___|___')
    
    print('\t\t   |   |   ')
    print(f'\t\t {polje_br[4]} | {polje_br[5]} | {polje_br[6]} ')
    print('\t\t___|___|___')
    
    print('\t\t   |   |   ')
    print(f'\t\t {polje_br[7]} | {polje_br[8]} | {polje_br[9]} ')
    print('\t\t___|___|___')

crtanje_ploce()

def status_igre():
    if polje_br[1]==polje_br[2]==polje_br[3]:
        return 1
    elif polje_br[4]==polje_br[5]==polje_br[6]:
        return 1
    elif polje_br[7]==polje_br[8]==polje_br[9]:
        return 1
    elif polje_br[1]==polje_br[5]==polje_br[9]:
        return 1
    elif polje_br[3]==polje_br[5]==polje_br[7]:
        return 1
    elif polje_br[1]==polje_br[4]==polje_br[7]:
        return 1
    elif polje_br[2]==polje_br[5]==polje_br[8]:
        return 1
    elif polje_br[3]==polje_br[6]==polje_br[9]:
        return 1
    elif (polje_br[1]!=1 and 
            polje_br[2]!=2 and 
            polje_br[3]!=3 and 
            polje_br[4]!=4 and 
            polje_br[5]!=5 and 
            polje_br[6]!=6 and
            polje_br[7]!=7 and
            polje_br[8]!=8 and
            polje_br[9]!=9 and
            ):
        return 0
    else:
        return -1

br_poteza=1
igrac=1
znak1='X'
znak2='O'

while br_poteza<=9:
    if igrac%2==1:
        igrac =1
    else:
        igrac =2

