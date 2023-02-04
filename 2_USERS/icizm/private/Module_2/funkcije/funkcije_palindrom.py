'''
while True: 
    rijec =input('Unesi riječ: ').lower()
    obrnuta_rijec = rijec[::-1]
    if not rijec: #ako nismo unijeli ništa
        break

    if rijec == obrnuta_rijec:             #ako smo unijeli riječ prvjeri jeli palindrom
        print('Riječ je palindrom!')
    else:
        print('Riječ NIJE palindrom')
'''

def otkrij_palindrom(rijec): 
    rijec = rijec.replace(' ', '')
    obrnuta_rijec = rijec[::-1]
    if rijec == obrnuta_rijec:             
        print('Riječ je palindrom!')
    else:
        print('Riječ NIJE palindrom')


rijec =input('Unesi riječ i provjeri da li je palindrom: ').lower()

