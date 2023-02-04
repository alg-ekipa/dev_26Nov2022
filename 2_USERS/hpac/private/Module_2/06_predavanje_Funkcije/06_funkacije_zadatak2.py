
def palindrom(rijec):
    obrnuta_rijec = rijec[::-1]
    if obrnuta_rijec == rijec:
        return 'Riječ je palindrom'
    else:
        return 'Riječ nije palindrom'

unesi_rijec = input('Unesi riječ: ').lower()
print(palindrom(unesi_rijec))
