
#aktivnost nad datotekama je append - dodaje na kraj
ime = input("Unesite ime: ")
prezime = input("Prezime: ")
mobitel = input("Mobitel: ")

#aktivnos nad datotekom je append - dodaje na kraj
file_writer = open("adresar.txt", "a")

#upisivanje sadržaja u datoteku

file_writer.write(f"Ime\tPrezime\tMobitel\n")
file_writer.write(f"{ime}\t{prezime}\t{mobitel}\n")

#zatvaranje datoteke
file_writer.close()

