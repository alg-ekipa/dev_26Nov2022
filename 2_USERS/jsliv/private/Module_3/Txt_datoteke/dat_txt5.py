

counter = 1

while True:
    ime = input("Unesite ime: ")
    prezime = input("Prezime: ")
    mobitel = input("Mobitel: ")

    try:
        with open("lkjglajhglahgčlahg") as file_writer #link za spremanje kod teacher
        redak = f"{counter}; {ime}; {prezime}; {mobitel}\n"
        file_writer.write(redak)
        counter += 1

    except Exception as e:
        print(f"Dogodila se pogreška {e}")

    if input("Unos novog ")