
# append dodaje na kraj datoteke upise

ime=input('Unesi ime: ')
prezime=input('Unesi prezime: ')
mobitel=input('Unesi mobitel: ')

file_writer = open('adresar.txt', 'a')          #otvaramo neposredno prije nego nam treba, prije upisujemo naredbe

#file_writer.write('Ime:\tPrezime:\tMobitel:\n')
file_writer.write(f'{ime}\t{prezime}\t{mobitel}\n')          #UPISIVANJE SADRŽAJA U DATOTEKU

file_writer.close               #zatvaranje datoteke

