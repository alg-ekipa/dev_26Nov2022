# DODAVANJE

ime = input('Unesi ime: ')
prezime = input('Unesi prezime: ')
mobitel = input('Unesi mobitel: ')

file_writer = open("adresar.txt", "a")  

# Upisivanje sadržaja u datoteku
#file_writer.write(f'Ime\tPrezime\tMobitel\n')
file_writer.write(f'{ime}\t{prezime}\t{mobitel}\n')

# Zatvaranje konekcije i otpuštanje resursa
file_writer.close()