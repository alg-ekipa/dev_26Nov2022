os_x = int(input('Koliko će brojeva biti na osi x: '))
os_y = int(input('Koliko će brojeva biti na osi y: '))

for i in range(1, os_y+1):
    for j in range(1, os_x+1):
        print(i*j, end='\t')
    print()