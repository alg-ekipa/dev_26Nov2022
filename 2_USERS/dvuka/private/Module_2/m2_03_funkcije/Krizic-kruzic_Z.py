tablica = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
nerijeseno = False

def igricaTraje():
    global nerijeseno
    # provjera: kombinacije

    # horizontalno
    if (tablica[0] == "x" and tablica[1] == "x" and tablica[2] == "x") or (tablica[0] == "o" and tablica[1] == "o" and tablica[2] == "o"): return False
    if (tablica[3] == "x" and tablica[4] == "x" and tablica[5] == "x") or (tablica[3] == "o" and tablica[4] == "o" and tablica[5] == "o"): return False
    if (tablica[6] == "x" and tablica[7] == "x" and tablica[8] == "x") or (tablica[6] == "o" and tablica[7] == "o" and tablica[8] == "o"): return False

    # vertikalno
    if (tablica[0] == "x" and tablica[3] == "x" and tablica[6] == "x") or (tablica[0] == "o" and tablica[3] == "o" and tablica[6] == "o"): return False
    if (tablica[1] == "x" and tablica[4] == "x" and tablica[7] == "x") or (tablica[1] == "o" and tablica[4] == "o" and tablica[7] == "o"): return False
    if (tablica[2] == "x" and tablica[5] == "x" and tablica[8] == "x") or (tablica[2] == "o" and tablica[5] == "o" and tablica[8] == "o"): return False

    # dijagonalno
    if (tablica[0] == "x" and tablica[4] == "x" and tablica[8] == "x") or (tablica[0] == "o" and tablica[4] == "o" and tablica[8] == "o"): return False
    if (tablica[2] == "x" and tablica[4] == "x" and tablica[6] == "x") or (tablica[2] == "o" and tablica[4] == "o" and tablica[6] == "o"): return False

    # ovdje računamo da je neriješeno ako ga loop ne promijeni, a loop ga ne mijenja ako su sva polja ispunjena
    traje = False
    
    for slot in tablica:
        if slot == " ":
            traje = True
            break

    nerijeseno = not traje
    return traje


def iscrtajTablicu():
    print(f"\n")
    print(f"\t     |     |")
    print(f"\t  {tablica[0]}  |  {tablica[1]}  |  {tablica[2]}")
    print(f'\t_____|_____|_____')
 
    print(f"\t     |     |")
    print(f"\t  {tablica[3]}  |  {tablica[4]}  |  {tablica[5]}")
    print(f'\t_____|_____|_____')
 
    print(f"\t     |     |")
    print(f"\t  {tablica[6]}  |  {tablica[7]}  |  {tablica[8]}")
    print(f"\t     |     |")
    print(f"\n")

def main():
    
    global tablica
    global nerijeseno

    ispunjeni = []

    prvi = ""
    while (prvi != "x" and prvi != "o"):
        prvi = input("Tko prvi kreće? x ili o? ")
    trenutni = prvi

    while(igricaTraje()):
        iscrtajTablicu()
        unos = int(input(f"{trenutni} unesite polje [1-9]: "))
        if tablica[unos - 1] != " ":
            print("To polje je već uneseno!")
            trenutni = trenutni == "x" and "o" or "x" # cheap trick za zamjenu tako da ostane isti igrac na sljedecoj rundi
        else:
            tablica[unos - 1] = trenutni
        trenutni = trenutni == "x" and "o" or "x"
    # igrica je zavrsila ovdje
    # opet moramo obrnuti igrača da bi dobili pravog pobjednika radi toga što ga je loop izmjenio na kraju
    trenutni = trenutni == "x" and "o" or "x"
    iscrtajTablicu()

    if nerijeseno:
        print("Igra je nažalost neriješena")
    else:
        print(f"Igra je gotova! Pobjednik je {trenutni}!")



main()