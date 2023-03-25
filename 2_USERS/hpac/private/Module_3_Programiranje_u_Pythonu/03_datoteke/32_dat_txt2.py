# Aktivnost nad datotekom je append - dodaje na kraj
file_writer = open('D:/HP/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/03_datoteke/ime.txt', 'a')

ime = input('Unesi ime i prezime: ')

# Upisivanje sadržaja u datotteku
file_writer.write(ime)

# zatvaranje konekcije i otpuštanje resursa
file_writer.close()

