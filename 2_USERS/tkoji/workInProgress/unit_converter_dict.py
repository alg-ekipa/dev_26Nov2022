
# TODO - in progress
unit_options = \
    {
        1: "Distance",
        2: "Temperature",
        3: "Weight",
        4: "Voulume",
        5: "Power",
    }

loop_control = True
while loop_control == True: 
    for k,v in unit_options.items():
        print("{:3}: {}".format(k,v))   
    change = int(input("\nWhich type of conversion you want to do. Choose 1 - 7 or 'q' to quit. ")) 
    
    inner_controller = True
    while inner_controller == True:
        if change == 1:
            length_dict = \
                {
                    1 : 'Kilometers',
                    2 : 'Miles',
                    3 : '< - Go back'
                }
            for k,v in length_dict.items():
                print("{:3}: {}".format(k,v))
                
            option = str(input("\nWhich type of distance conversion you want to do. Choose 1 - 2. "))
            if option.isdigit():
                option = int(option)

            if option == 1:
                print("Option 1.")
                conversion = int(input("Input kilometer number: "))
                # TODO - dummy input, demonstration math only.
                print(f'{ conversion } km are equal to { conversion * 123.123 } miles.')
                inner_controller = False
            elif option == 2:
                print("Option 2.")
                conversion = int(input("Input miles number: "))
                # TODO - dummy input, demonstration math only.
                print(f'{ conversion } miles are equal to { conversion / 123.123 } kilometers.')
            elif option == 3:
                 inner_controller = False
                 break
            else:
                while True:
                    print("Incorrect input")
                    choice = input("Choose if you wish to continue or quit ( yes/no )?").lower()
                    if choice == 'y' or choice == 'yes':
                        break
                    if choice == 'n' or choice == 'no':
                        inner_controller = False
                        loop_control = True
                        break
                    
            1