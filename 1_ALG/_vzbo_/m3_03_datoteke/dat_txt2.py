
# aktivnost nad datotekom je append - dodaje na kraj

ime = input("Unesi ime: ")
prezime = input("Prezime: ")
mobitel = input("Mobitel: ")

# aktivnost nad datotekom je append - dodaje na kraj
file_writer = open("adresar.txt", "a")
# upisivanje sadržaja u datoteku
#file_writer.write(f'Ime\tPrezime\tMobitel\n')
file_writer.write(f'{ime}\t{prezime}\t{mobitel}\n')

# zatvaranje konekcije i otpuštanje resursa
file_writer.close()