play = input("Do you wish to play? Enter y or n. ")
count = 0

while play == 'y': 
    secret_number = 21
    guess = int(input("Please input your number: "))
    if secret_number < guess:
        print("Your number is bigger than secret number")
        count = count + 1
    elif secret_number > guess:
        print("Your numnber is smaller than secret number")
        count = count + 1
    else:
        print("Bravooo!")
        count = count + 1
        print("Total count:", count)
        play = input("Do you want to start again? Enter y or n.")
        if play == 'y':
           pass
           count = 0
        else:
            print("Thanks for playing my game. Goodbye!")
            break
        

