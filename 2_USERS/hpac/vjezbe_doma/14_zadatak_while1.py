# Unesi password

password = 'burek'

while True:
    unos = input('Unesi šifru: ')
    if unos == password:
        print('Unijeli ste dobru šifru!!!')
        break
    else:
        print('Unešeno ja kriva šifra!! Pokušajte ponvno')