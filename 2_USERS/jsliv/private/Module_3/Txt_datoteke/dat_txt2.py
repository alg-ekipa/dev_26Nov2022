
save_path = 'D:/VisualStudioCode/Juli/dev_26Nov2022/2_USERS/jsliv/private/Module_3/Txt_datoteke/adresar.txt'
file_weiter = open(save_path, "a")


#aktivnost nad datotekama je append - dodaje na kraj
ime = input("Unesite ime: ")
prezime = input("Prezime: ")
mobitel = input("Mobitel: ")

#aktivnos nad datotekom je append - dodaje na kraj
file_writer = open("adresar.txt", "a")

#upisivanje sadržaja u datoteku

#file_writer.write(f"Ime\tPrezime\tMobitel\n")
file_writer.write(f"{ime}\t{prezime}\t{mobitel}\n")

#zatvaranje datoteke
file_writer.close()

