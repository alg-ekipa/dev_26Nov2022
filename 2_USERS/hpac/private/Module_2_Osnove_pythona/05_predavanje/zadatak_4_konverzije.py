# potrebno je napraviti program za konverziju  u oba smjera
# 1km = 0,6214 milje
# 0C = 0F -->  Tf = Tc*9/5 + 32
# 1kg = 2,2046pounds
# 1l = 0,2642 US gal
# 1kW = 1,3596KS

print('Ovo će ti pomoći pri konverziji jedinica.')
print('Koju konverziju želite odraditi:\n\t1. udaljenost\n\t2. temperatura\n\t3. masa\n\t4. volumen\n\t5. snaga')
odluka = int(input('Napišite broj koji se nalazi ispred željene konverzije: '))

while odluka in range(1,5):
    if odluka == 1:
        print('Koju konverziju želite:\n\ta. km u milje\n\tb. milje u km')
        odluka_2 = input('Napišite slovo koji se nalazi ispred željene konverzije: ')
        if odluka_2 == 'a':
            print('Unesite broj kilometara: ')
            broj = float(input())
            print(f'{broj} km iznosi {broj*0.6214}milja')
        if odluka_2 == 'b':
            print('Unesite broj milja: ')
            broj = float(input())
            print(f'{broj} km iznosi {broj/0.6214}milja')
        else:
            break
    if odluka == 2:
        print('Koju konverziju želite:\n\ta. C -> F\n\tb. F - > C')
        odluka_2 = input('Napišite slovo koji se nalazi ispred željene konverzije: ')
        if odluka_2 == 'a':
            print('Unesite stupnjeve Celziusa: ')
            broj = float(input())
            print(f'{broj} C iznosi {broj*9/5+32}F')
        if odluka_2 == 'b':
            print('Unesite stupnjeve Farheheit: ')
            broj = float(input())
            print(f'{broj} F iznosi {(broj-32)*5/9}C') 
        else:
            break    
    if odluka == 3:
        print('Koju konverziju želite:\n\ta. kg -> pounds\n\tb. pounds -> kg')
        odluka_2 = input('Napišite slovo koji se nalazi ispred željene konverzije: ')
        if odluka_2 == 'a':
            print('Unesite broj kilograma: ')
            broj = float(input()) 
            print(f'{broj} kg iznosi {broj*2.2046} pounds')
        if odluka_2 == 'b':
            print('Unesite broj pounds-a: ')
            broj = float(input())
            print(f'{broj} pounds iznosi {broj/2.2046} kg') 
        else:
            break     
    else:
        break

