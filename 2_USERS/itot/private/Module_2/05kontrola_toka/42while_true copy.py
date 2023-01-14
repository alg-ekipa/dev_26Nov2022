'''break pass contuine'''

while True:
    print('Sada smo u potencionalno beskonacna petlja')

    odgovor = int(input(' zelite li prekinuti petulju? 1-DA. 0- NE   '))

    if odgovor == 1:
        print('Potencijalno beskonacna petlja je prekinuta!')
        break

    else:
        pass


niz = 'Paython Programer' # kod 'g' je izasao iz petlje
for slovo in niz:
    if slovo == 'g':
        break
    print( slovo, end=' ')
print()

niz = 'Paython Programer'  # 'g' je preskocio, pa nastavio dalje
for slovo in niz:
    if slovo == 'g':
        continue
    print( slovo, end=' ')
print()