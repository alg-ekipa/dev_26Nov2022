import random as rd

#slova: od 65 do 90 i 97 do 122 ASCII table
#brojevi: od 48 do 57
#znakovi: od 33 do 47, 58-64, 91-96, 123-126

def generiraj_lozinku(odabir):
    lozinka=''
    duljina_lozinke= int(input('Unesi duljinu lozinke: '))

    for i in range(duljina_lozinke):
        #odabir 1: slova
        if odabir ==1:
            a=rd.choice([(65,90), (97,122)])
        elif odabir==2:
            a=rd.choice([(48,57)])
        elif odabir==3:
            a=rd.choice([(33,47), (58,64), (91,96)])

        broj=rd.randint(*a)
        znak = chr(broj)
        lozinka+=znak
    return(lozinka)


print('IZBORNIK')
print('1 - slova, 2 - brojevi, 3 - znakovi')
print()
izbor = int(input('Unesi izbor: '))
print(generiraj_lozinku(izbor))


