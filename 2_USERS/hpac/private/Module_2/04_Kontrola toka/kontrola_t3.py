# PALINDROM - isto se čita lijevo i desno (ivolavalovi) - slide 95 4.dio
'''
rijec = 'zagreb'


obrnuta_rijec = rijec[::-1]
print(obrnuta_rijec)
'''
rijec = input('Unesi rijec: ')
obrnuta_rijec = rijec[::-1]

if obrnuta_rijec == rijec:
    print('Riječ JE palindrom!!')
else:
    print('Riječ NIJE palindrom')