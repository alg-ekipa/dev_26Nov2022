'''
for i in range(1, 11, 1):       #range(START : STOP-1: STEP)
    print(i)                    #ako nema START on je 0, ako nema STEP on je 1

for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(0,11,2):
    print(i)

for i in range(1, 101,2):
    print(i, end=' ')

for i in range(1,101):
    print(i,end=' ')

for i in range(50,101,5):
    print(i,end=' ')

for i in range(100,-1,-5):
    print(i, end=' ')
'''

#Zbroj # od 1 do 20

zbroj = 0
for i in range (21):
    #print(i, end=' ')
    zbroj=zbroj+i
    #print(zbroj, end=' ')
print(f'Završni zbroj je {zbroj}')

for i in range(11):
    print(i)