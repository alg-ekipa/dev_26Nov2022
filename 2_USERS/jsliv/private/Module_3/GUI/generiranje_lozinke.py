import random as rd

#ASCII table
#slova: 65 - 90 i 97 - 122
#brojevi: 48 - 57
#znakovi: 33 - 47 i 91 - 96





def generiraj_lozinku(odabir):

    lozinka = ""

    duljina_lozinke = int(input("Unesi duljinu lozinke: "))

    for znak in range(duljina_lozinke):
        if odabir == 1:
            a = rd.choice([(65, 90), (97, 122)])
        elif odabir == 2:
            a = rd.choice([(48, 57)])
        elif odabir == 3:
            a = rd.choice([(33,47), (58,64), (91,96)])
        
        broj = rd.randint(*a)
        znak = chr(broj)
        lozinka += znak
    
    return lozinka
    

print("IZBORNIK")
print("1 Slova, 2 Brojevi, 3 Znakovi")

izbor = int(input("Unesi izbor: "))
print(generiraj_lozinku(izbor))