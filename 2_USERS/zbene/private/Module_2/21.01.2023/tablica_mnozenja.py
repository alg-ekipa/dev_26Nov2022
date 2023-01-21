'''for i in range (1,11):
    for j in range (1,11):
        print(i*j, end='\t')
    print()
'''
x = int (input('Unesi željeni broj stupaca: '))
y = int (input ('Unesi željeni broj redaka: '))
for i in range (1, x+1):
    for j in range (1, y+1):
        print(i*j, end='\t')
    print()