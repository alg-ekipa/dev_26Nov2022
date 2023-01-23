import random

CRED = '\033[91m'
CEND = '\033[0m'
CYEL = '\33[43m'
CEND =  '\033[0m'

#game = input("Do you want to play? ")
game =  'y'
count_user = 0
count_computer = 0
count_tie = 0 

game_options = {
    1 : 'rock',
    2 :'scissors',
    3 :'paper'
}

print(game_options)

while game == 'y':
    choice_computer = random.randrange(1,3).
    
    choice_user = str(input('''\nLet's play. Input the number or 'q' to exit the game.
        1) Rock
        2) Scissiors
        3) Paper\n
        Enter your choice: '''))
    if choice_user.isdigit():
        choice_user = int(choice_user)
    else:
         choice_user = str(choice_user).lower()
         
    if choice_user == choice_computer:
        print(CYEL + "Tie, non of the users got the point" + CEND)
        
    elif choice_user == 1 and choice_computer == 2:
         print(CYEL + "User won." + CEND)
         count_user += 1
    
    elif choice_user == 1 and choice_computer == 3:
        print(CYEL + "Computer won." + CEND)
        count_computer += 1
        
    elif choice_user == 2 and choice_computer == 1:
        print(CYEL +"Computer won." + CEND)
        count_computer += 1
    
    elif choice_user == 2 and choice_computer == 3:
        print(CYEL +"Computer won." + CEND)
        count_computer += 1      
        
    elif choice_user == 3 and choice_computer == 1:
         print(CYEL +"User won." + CEND)
         count_user += 1
    
    elif choice_user == 3 and choice_computer == 2:
         print(CYEL +"Computer won." + CEND)
         count_computer += 1
    
    elif choice_user == 'q':
        print("\nThanks for playing. The result is below.\n")
        break
    else:
        print(CRED, "Invalid input, please choose the options from the menu or type 'q' to quit.", CEND)

print(f'User: {count_user}\nComputer: {count_computer}')
