import os

polje = [1,2,3,4,5,6,7,8,9]

def ploca_za_igranje():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\t ',polje[0],'|',polje[1],'|',polje[2])
    print('\t ',polje[3],'|',polje[4],'|',polje[5])
    print('\t ',polje[6],'|',polje[7],'|',polje[8])

def igra():
    if polje[0] == polje[1] ==polje[2]:
        return 1
    elif polje[3] == polje[4] ==polje[5]:
        return 1
    elif polje[6] == polje[7] ==polje[8]:
        return 1
    elif polje[0] == polje[3] ==polje[6]:
        return 1
    elif polje[1] == polje[4] ==polje[7]:
        return 1
    elif polje[2] == polje[5] ==polje[8]:
        return 1
    elif polje[0] == polje[4] ==polje[8]:
        return 1
    elif polje[2] == polje[4] ==polje[6]:
        return 1
    else:
        return 0 #nerješeno

#print(ploca_za_igranje())

