rijec = 'programiranje' #string se može tretirati kao lista

for slovo in rijec: 
    print(slovo, end = ' ')

    #može li se len primjeniti? 
print()
print(f'Broj slova u riječi {rijec} je {len(rijec)}.')

rijec_lista = list(rijec)
print(rijec_lista)