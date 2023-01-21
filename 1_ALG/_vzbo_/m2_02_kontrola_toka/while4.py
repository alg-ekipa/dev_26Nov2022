'''while 1:
    broj = int(input('Unesi cijeli broj: '))
    print(f'Dvostruki iznos unesenog broja je {2*broj}')


'''
# ako ne napravimo nikakav unos, program će izbaciti s greškom
# kako to riješiti? stavimo uvjet nakon unosa
while 1:
    broj = input('Unesi cijeli broj: ')
    if not broj:
        break
    print(f'Dvostruki iznos unesenog broja je {2*int(broj)}')
    if not broj:
        break

