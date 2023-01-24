import random
secret_number = random.randrange(1,100)

play = input("Wanna guess my secret number?\nEnter 'y' to play or 'n' to quit. ").lower()

while play != 'y':
    if play == 'y':
        pass
    elif play == 'n':
        print("See you next time.")
    else:
        print("Invalid input.")
        play = input("Enter 'y' to play a game or 'n' to quit. ").lower()
    
count = 0

# TODO - error handling isn't resolved yet.

while play == 'y':
    guess = str(input("Please input your number in range 1 - 100: "))
    while guess.isdigit() == False:
        print("Invalid input! Only digits in range 1 - 100 are allowed.")
        guess = str(input("Please input your number: "))
        count = count + 1
    if int(guess) > 100:
        print("Number out of range. Please input a number in the range 1 - 100. ")
        guess = str(input("Please input your number: "))
        count = count + 1
    if int(guess) < secret_number:
        print("Your guess is lower than a secret number")
        count = count + 1
    elif int(guess) > secret_number:
        print("Your guess is greater than a secret number")
        count = count + 1
    else:
        count = count + 1
        print(f'Congratulations!!!\nYou the secret number in \"{count}\" attempt(s).\n')        
        count = 0
        while True:
            play = input("Do you want to play again? Enter 'y' to play or 'n' to quit. ").lower()
            if play == 'y':
                play == 'y'
                break
            elif play == 'n':
                print("See you next time.")
                break
            else:
                print("Invalid input.")
                pass
            
            