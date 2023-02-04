
# Coloring.
CRED = '\033[91m'
CEND = '\033[0m'

unit_options = \
    {
        1: "Distance",
        2: "Temperature",
        3: "Weight",
        4: "Voulume",
        5: "Power",
    }

def miles_to_kilometers()

main_menu_loop_control = True
while main_menu_loop_control == True: 
    for k,v in unit_options.items():
        print("{:3}: {}".format(k,v))   
    change = str(input("\nWhich type of conversion you want to do. Choose 1 - 7 or 'q' to quit. ")) 
    
    if not change.isdigit():
        if change == 'q':
            break
        else:
            continue
    else: 
        change = int(change)
    
    sub_menu_loop_control = True
    while sub_menu_loop_control == True:
        if change == 1:
            length_dict = \
                {
                    1 : 'Kilometers',
                    2 : 'Miles',
                    3 : '< - Return'
                }
            for k,v in length_dict.items():
                print("{:3}: {}".format(k,v))
                
            option = str(input("\nWhich type of distance conversion you want to do. Choose 1 - 2. "))
            if option.isdigit():
                option = int(option)

            if option == 1:
                conversion = float(input("Input kilometer number: "))
                print(f'{ conversion } km are equal to { round(conversion * 0.62137, 2) } miles.')
                sub_menu_loop_control = False
            elif option == 2:
                conversion = float(input("Input miles number: "))
                print(f'{ conversion } miles are equal to { round(conversion / 0.62137, 2) } kilometers.')
            elif option == 3:
                 sub_menu_loop_control = False
                 break
            else:
                while True:
                    choice = input("Incorrect input. Do you wish to continue ( yes / no )? ").lower()
                    if choice == 'y' or choice == 'yes':
                        break
                    if choice == 'n' or choice == 'no':
                        sub_menu_loop_control = False
                        main_menu_loop_control = True
                        break
        
        if change == 2:
            length_dict = \
                {
                    1 : 'Celcius',
                    2 : 'Ferenheits',
                    3 : '< - Return'
                }
            for k,v in length_dict.items():
                print("{:3}: {}".format(k,v))
                
            option = str(input("\nWhich type of distance conversion you want to do. Choose 1 - 2. "))
            if option.isdigit():
                option = int(option)

            if option == 1:
                conversion = float(input("Input a temparature in degrees Clesius: "))
                print(f'{ conversion } degrees Clesius are equal to { round(( conversion  * 1.8 ) + 32, 2) } Ferenheits.')
                sub_menu_loop_control = False
            elif option == 2:
                conversion = float(input("Input a temperature in degrees Ferenheits: "))
                print(f'{ conversion } degrees Ferenheits are equal to { round((conversion - 32) / 1.8, 2) } Celcius.')
            elif option == 3:
                 sub_menu_loop_control = False
                 break
            else:
                while True:
                    choice = input("Incorrect input. Do you wish to continue ( yes / no )? ").lower()
                    if choice == 'y' or choice == 'yes':
                        break
                    if choice == 'n' or choice == 'no':
                        sub_menu_loop_control = False
                        main_menu_loop_control = True
                        break
                    
print("End of the program.")
# TODO 
# - configure other conversion types
# - request code review