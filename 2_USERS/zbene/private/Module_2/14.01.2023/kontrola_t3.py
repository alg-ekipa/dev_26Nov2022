# PALINDROM (slide 95, 04dio 02 osnove programiranja)

#rijec = 'Zagreb'
#print (rijec [::-1])

rijec = input ('Unesi riječ: ')
obrnuta_rijec = rijec [::-1]
if obrnuta_rijec == rijec:
    print ('Riječ je palindrom!')
else:
    print('Riječ nije palindrom')