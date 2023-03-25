counter = 1

while True:
    ime = input("Unesite ime: ")
    prezime = input("Prezime: ")
    mobitel = input("Mobitel: ")

    file_writer = open("  link  ", "a")
    file_writer.write(f"{counter};{ime};{prezime};{mobitel}")
    counter +=1

    file_writer.close()

    if input("Novi? ") !="da":
        break