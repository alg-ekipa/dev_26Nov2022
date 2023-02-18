# break, continue i pass

while True: #moraju biti velika slova
    print('Sada smo u potencijalno beskonačnoj petlji')

    odgovor = int(input('Želite li prekinuti petlju? 1-DA, 0-NE '))
    
    if odgovor == 1:
        print('Potencijalno beskonačna petlja je prekinuta!')
        break #perekidamo petlju

    else: 
        pass 


niz = 'Python Programer'
for slovo in niz:
    if slovo == 'g':
        break
    print(slovo, end=' ') #staje kad dođe do slova g
print()

for slovo in niz:
    if slovo == 'g':
        continue
    print(slovo, end=' ') #printa bez g
print()

