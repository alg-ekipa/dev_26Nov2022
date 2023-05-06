import random as rd

#slova: od 65 do 90 i 97 do 122
#brojevi:od 48 do 57
#znakovi: od 33-47, 58-64, 91-96


def generiraj_lozinku(odabir):

    lozinka=''

    duljina_lozinka=int(input('Unesi duljinu lozinke: '))

    for znak in range(duljina_lozinka):
        #odabir 1:slova
        if odabir ==1:
            a=rd.choice([(65,90),(97,122)])
        #odabir 2:brojevi
        elif odabir==2:
            a=rd.choice([(48,57)])
        #odabir 3:znakovi
        elif odabir==3:
            a=rd.choice([(33,47),(58,64),(91,96)])

        broj=rd.randint(*a)
        znak=chr(broj)
        lozinka+=znak

        return lozinka

print('IZBORNIK')
print('1 - slova, 2 - brojevi, 3 - znakovi')

izbor=int(input('Unesi izbor: '))
print(generiraj_lozinku(izbor))