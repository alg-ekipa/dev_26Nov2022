import random

#game = input("Do you want to play? ")
game =  'y'

count_user = 0
count_computer = 0

while game == 'y':
    choice_computer = random.randrange(1,3)
    print("Computer choose", choice_computer)
    choice_user = str(input('''Let's play. Input the number or 'q' to exit the game.
        1) Rock
        2) Scissiors
        3) Paper\n
        Enter your choice: '''))
    if choice_user.isdigit():
        choice_user = int(choice_user)
    else:
         choice_user = str(choice_user)

    if choice_user == choice_computer:
        print("X, not of the users gets the point")
        count_user = 0
        count_computer = 0
        continue
    elif choice_user == 1 and choice_computer == 2:
         print("User won.")
         count_user += 1
    
    elif choice_user == 1 and choice_computer == 3:
        print("Computer won.")
        count_computer += 1
        
    elif choice_user == 3 and choice_computer == 1:
         print("User won.")
         count_user += 1
    
    elif choice_user == 3 and choice_computer == 2:
         print("Computer won.")
         count_computer += 1
    
    elif choice_user == 2 and choice_computer == 1:
        print("Computer won.")
        count_computer += 1
    
    elif choice_user == 'q':
        print("Thanks for playing. The result is below.\n")
        break
    else:
        print("Invalid input.")
        break

print(f'User: {count_user}\nComputer: {count_computer}')
