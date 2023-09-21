def unos_filma():
    naziv_filma = input("Unesi naziv filma: ")
    ocjena_filma = input("Unesi ocjenu filma: ")

    return naziv_filma, ocjena_filma

def main():
    naziv, ocjena = unos_filma()

    print("Naziv filma je: ", naziv)
    print("Film ima ocjenu: ", ocjena)

if __name__ == "__main__":
    main()