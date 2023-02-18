#PALINDROM


rijec=input('Unesi rijeČ: ')

obrnuta_rijec=rijec[::-1]
#print(obrnuta_rijec)

if obrnuta_rijec==rijec:
    print('Riječ je palindrom!')
else:
    print('Riječ NiJE palindrom')


