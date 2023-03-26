# Aktivnost nad datotekom je append - dodaje na kraj


ime = input('Unesi ime: ')
prezime = input ('Unesi prezime: ')
mobitel = input('Mobitel: ')

file_writer = open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/adresar.txt', 'a')

# Upisivanje sadržaja u datotteku

#file_writer.write(f'Ime\tPrezime\tMobitel\n')
file_writer.write(f'{ime}\t{prezime}\t{mobitel}\n')

# zatvaranje konekcije i otpuštanje resursa
file_writer.close()
