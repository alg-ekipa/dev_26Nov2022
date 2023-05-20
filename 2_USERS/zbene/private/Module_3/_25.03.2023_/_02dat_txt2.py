# Aktivnost nad datotekom je append - dodaje na kraj


ime = input('Unesi ime: ')
prezime = input ('Unesi prezime: ')
mobitel = input('Mobitel: ')

file_writer = open('D:/python 26.11. grupa/dev_26Nov2022-1/2_USERS/zbene/private/Module_3/25.03.2023/adresar.txt', 'a')

# Upisivanje sadržaja u datotteku

#file_writer.write(f'Ime\tPrezime\tMobitel\n')
file_writer.write(f'{ime}\t{prezime}\t{mobitel}\n')

# zatvaranje konekcije i otpuštanje resursa
file_writer.close()
