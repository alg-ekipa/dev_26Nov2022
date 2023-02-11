broj_kartice=input('unesi broj kartice ')
zakodirani_broj_kartice=''

print ('unesite znak za maskiranje broja kartice:')
znak=input()
duljina=len(broj_kartice)
i=0




for slovo in broj_kartice:

    print(slovo,end= ' ')
    i=i+1
    if i>(duljina-4): 
        zakodirani_broj_kartice=zakodirani_broj_kartice+slovo
    elif slovo=='-':
        zakodirani_broj_kartice=zakodirani_broj_kartice+slovo
    else:
        zakodirani_broj_kartice=zakodirani_broj_kartice+znak




print()

print(f'broj znamenaka u broju kartice \n{broj_kartice} je {duljina}')
print(f'zakodirani broj kartice je \n{zakodirani_broj_kartice}')

