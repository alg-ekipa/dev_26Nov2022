

miles = 0.6214

def f_miles_to_km(num):
    f_value = round(num * miles,2)
    return f_value

def f_km_to_miles(num):
    f_value = round(num / miles,2)
    return f_value

def f_celcius_to_ferenheits(num):
    f_value = round((num * 1.8 ) + 32, 2)
    return f_value
    
def f_ferenheits_to_celcius(num):
    f_value = round((num - 32) / 1.8, 2)
    return f_value

        
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
                result = f_km_to_miles(conversion)
                print(f'{ conversion } kms are equal to {result} miles.\n')
                sub_menu_loop_control = False
            elif option == 2:
                conversion = float(input("Input miles number: "))
                result = f_miles_to_km(conversion)
                print(f'{ conversion } miles are equal to {result} kilometers.\n')
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
                result = f_celcius_to_ferenheits(conversion)
                print(f'{ conversion } degrees Clesius are equal to {result} Ferenheits.\n')
                sub_menu_loop_control = False
            elif option == 2:
                conversion = float(input("Input a temperature in degrees Ferenheits: "))
                result = f_ferenheits_to_celcius(conversion)
                print(f'{ conversion } degrees Ferenheits are equal to {result} Celcius.\n')
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
# # TODO 
# # - configure other conversion types
# # - request code review