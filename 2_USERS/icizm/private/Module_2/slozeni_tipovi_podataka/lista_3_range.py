# i je pomoćna varijabla - ITERATOR

for i in range(0, 11, 2):       #range(START : STOP-1 : STEP) ako je step izostavljen, po difoltu je 1 
    print(i)

for i in range(1, 101):       
    print(i, end=' ')

print ()

for i in range(100, -1, -5):      #unazad, moramo staviti -1 ako želimo uloviti 0 
    print(i, end=' ')
