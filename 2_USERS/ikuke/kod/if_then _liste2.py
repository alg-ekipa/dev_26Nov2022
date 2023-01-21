#PALINDROM

rijec= 'Zagreb'
#rijec = input ('Unesi rijec:')




print(f'duljina rijeci {rijec} je {len(rijec)}')
duljina_rijeci=len(rijec)

for slovo in rijec: # za svako slovo unutar rijeci -- RIJEC je vec lista -- odnosno svaki string je lista
    print(slovo)
palindrom=[]
i=0



for slovo in rijec:
    palindrom.append(rijec[duljina_rijeci-i-1])
    i=i+1
print(f'duljina rijeci {palindrom} je {len(palindrom)}')


print (palindrom)

for slovo in palindrom: # za svako slovo unutar rijeci -- RIJEC je vec lista -- odnosno svaki string je lista
    print(f'{slovo}', end='')
palindrom=[]
i=0

print()
print("--------------------------------------------------------------------------------------------")

tekst= ('Lorem . ipsum . dolor sit amet, consectetur adipiscing elit, sed . do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

tekst1 = tekst.lower()
print (tekst)
lista_rijeci = tekst1.split()
print (lista_rijeci)
print (lista_rijeci[0].replace('lorem', 'igor'))
lista_rijeci[0].replace('lorem', 'igor')

print (lista_rijeci)


for rijec in lista_rijeci:
    if '.' in rijec:
        lista_rijeci[lista_rijeci.index(rijec)] = rijec.replace('.','')



print (lista_rijeci)