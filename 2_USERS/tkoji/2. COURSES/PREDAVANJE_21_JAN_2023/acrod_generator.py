
tone = ["C", "D", "E", "F", "G", "A", "H"]

print("Printing DUR and MOL tones...")
print(f"DUR: { tone[0] },{ tone[3] },{ tone[4] }.")
print(f"MOL: { tone[1] },{ tone[2] },{ tone[6] }.\n")
play = 'y'
while play == 'y':
    number = int(input("Please add a first accord number to find a scale: "))
    if number in [1,2,3,4,5,6,7]:
        if not number:
            break
        if number == 1:
            print(f"Number {number}st accord corresponds DUR tone: { tone[0]}")
            
        if number == 2:
            print(f"Number {number}nd accord corresponds MOL tone: { tone[1] }.")
            
        if number == 3:
            print(f"Number {number}rd accord corresponds MOL tone: { tone[2] }.")
            
        if number == 4:
            print(f"Number {number}th accord corresponds DUR tone: { tone[3] }.")
            
        if number == 5:
            print(f"Number {number}th accord corresponds DUR tone: { tone[4] }.")
            
        if number == 7:
            print(f"Number {number}th accord corresponds MOL tone: { tone[6] }.")
            
        if number in [6]:
            print(f"A tone '{number}' is not is not in MOL or DUR scale.")
            
    else:
        print("Number not in range.")
        play_again = input("If you wish to continue press 'y', for exit press 'q'")
        play = 'n'
        while play_again == 'y':
            if play_again == 'y':
                play = 'y'
                break
            elif play_again == 'q':
                break
            else: 
                print("Incorrent input, try again.")
                
