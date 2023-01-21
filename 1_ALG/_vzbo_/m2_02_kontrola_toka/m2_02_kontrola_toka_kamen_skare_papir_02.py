from random import randint 

izbor = ['kamen', 'škare', 'papir']
player2 = izbor[randint(0,2)]

broj_pobjeda = 0
broj_pobjeda2 = 0

player1 = True
while player1 == True:
    player1 = input('kamen, škare, papir? (Završi igru: kraj)')
    
    if player1 == player2:
        print('Neriješeno!')
        
    elif player1 == 'kamen':
        if player2 == 'papir':
            print('Izgubio si!')
            broj_pobjeda2 += 1
        else:
            print('Pobijedio si!')
            broj_pobjeda += 1
            
    elif player1 == 'papir':
        if player2 == 'škare':
            print('Izgubio si!')
            broj_pobjeda2 += 1
        else:
            print('Pobijedio si!')
            broj_pobjeda += 1
            
    elif player1 == 'škare':
        if player2 == 'kamen':
            print('Izgubio si!')
            broj_pobjeda2 += 1
        else:
            print('Pobijedio si!')
            broj_pobjeda += 1
            
    elif player1 == 'kraj':
        print(f'Završni rezultat:\n(P1) {broj_pobjeda} VS {broj_pobjeda2} (P2)')
        
    else:
        print('Riječ koju st upisali ne koristi se u ovoj igri! Probajte ponovno!')
    player1=True

