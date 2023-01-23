import random

CRED = '\033[91m'
CEND = '\033[0m'
CYEL = '\33[43m'
CEND =  '\033[0m'

game = input("Do you want to play? ")
game =  'y'
count_user = 0
count_computer = 0
count_tie = 0 

while game == 'y':
    rounds = int(input("How many rounds you want to play? "))
    game_count = 0
    while game_count < rounds: 
        choice_computer = random.randrange(1,4)
        print("Computer choose", choice_computer,'\n')
        choice_user = str(input('''Let's play! Input the number or 'q' to exit the game.
            1) Rock
            2) Scissiors
            3) Paper\n
            Enter your choice: '''))
        if choice_user.isdigit():
            choice_user = int(choice_user)
        else:
            choice_user = str(choice_user).lower()
        if choice_user == choice_computer:
            print(CYEL + "Tie, non of the users gets the point." + CEND)
            count_tie += 1 
            game_count += 1
            
        elif choice_user == 1 and choice_computer == 2:
            print(CYEL + "User won." + CEND)
            count_user += 1
            game_count += 1
            
        elif choice_user == 1 and choice_computer == 3:
            print(CYEL + "Computer won." + CEND)
            count_computer += 1
            game_count += 1
                     
        elif choice_user == 2 and choice_computer == 1:
            print(CYEL +"Computer won." + CEND)
            count_computer += 1
            game_count += 1
                  
        elif choice_user == 2 and choice_computer == 3:
            print(CYEL +"Computer won." + CEND)
            count_computer += 1      
            game_count += 1
            
        elif choice_user == 3 and choice_computer == 1:
            print(CYEL +"User won." + CEND)
            count_user += 1
            game_count += 1
               
        elif choice_user == 3 and choice_computer == 2:
            print(CYEL +"Computer won." + CEND)
            count_computer += 1
            game_count += 1
               
        elif choice_user == 'q':
            print("\nThanks for playing. The result is below.\n")
            break
        else:
            print(CRED + "Invalid input, please choose the options from the menu or type 'q' to quit." + CEND)
    break
print(f"\nEnd of the game. Here are the game statistics played in {rounds} round(s).")
print(f'USER: {count_user}\nCPU: {count_computer}\nTIE: {count_tie}')