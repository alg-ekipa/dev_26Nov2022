
# BREAK, CONTINUE, PASS

"""
while True:
    print('Sada smo u potencijalnop beskonačnoj petlji')

    odgovor = int(input('Želite li prekinuti petlju? 1-DA, 0-NE '))

    if odgovor ==1:
        print('Potencijano beskonačna petlja je prekinuta.')
        break

    else:
        pass

"""
"""
niz  = 'Phyton Programer'
for slovo in niz:                 BREAK - PREKIDA PRIJE SLOVA I IZLAZAK IZ PETLJE
    if slovo == 'g':
        break
    print(slovo, end=' ')
print()
"""
"""
niz  = 'Phyton Programer'
for slovo in niz:
    if slovo == 'g':                CONTINUE - PRESKAČE TO SLOVO
        continue
    print(slovo, end=' ')
print()
"""



