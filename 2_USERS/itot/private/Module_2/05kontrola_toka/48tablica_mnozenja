#play = input("Do you wish to play? Enter y or n. ")
play = 'Y'
miles = 0.6214
pounds = 2.2046
option = 0
option_rule = (1,2,3,4,5,6,7,8,9,10)

def test_fl(enter): # provjera je li broj float
    is_number=enter.replace(",", ".")
    try:
        float(is_number)
        return True
    except ValueError:
        return False


def test_game(game):  # provjera zelis li novu igru
    while game.upper() not in ["N","Y"]:
        game = input('Pogrešan unos. Želite li novu igru? N - ne; Y - da: ')
    if game.upper() in ["N","Y"]:
        return True



while play.upper() == "Y":  # itot: Eliminitrao sam malo/veliko slovo
    option = str(input('''Please enter the number for desired conversion: 
        \n1. Kilometers to miles.
        \n2. Miles to kilometers.
        \n3. Kilogram to pounds.
        \n4. Pounds to kilograms.
        \n5. Celcius to Ferenheits
        \n6. Ferenheits to Celcius
        \n7. Listers to gallons
        \n8. Gallons to liters
        \n9. Kilowatts to horsepower
        \n10. Horsepower to kilowattsa
        
        \nYour input here: '''))
        ##### START OF KM - MILES CONVERSION #####
        
            ### provjera je li broj 1 - 10   
    while  option.isdigit() == False or int(option) not in option_rule:
        option = input('The input is not good, please re-enter option 1 - 10: ')

            # "intput" je naredba, ne može biti i varijbla
    if int(option) in option_rule:
        option = int(option)

        if option == 1:
            enter = input("Input the km number: ")
            while test_fl(enter) == False:
                enter = input("Pease enter NUMBER of km: ")
            while test_fl(enter) == True:
                enter_f=float(enter.replace(",", "."))
                print(f'Enter u TRUE {enter_f}')
                print(f'{enter_f} km are equal to {enter_f * miles} miles.')
                game = input('Do you wont new game? N - no; Y- yes: ')
                if test_game(game) == True:
                    play=game
                    break

        if option == 2:
            enter = input("Input the miles number: ")
            while test_fl(enter) == False:
                enter = input("Pease enter NUMBER of miles: ")
            while test_fl(enter) == True:
                enter_f=float(enter.replace(",", "."))
                print(f'Enter u TRUE {enter_f}')
                print(f'{enter_f} miles are equal to {enter_f / miles} miles.')
                game = input('Do you wont new game? N - no; Y- yes: ')
                if test_game(game) == True:
                    play=game
                    break
                
            
        ###########################################
        
        '''
        ##### START OF KG - POUNDS CONVERSION #####
        elif option == 3: 
            input = int(input("Input the kg number: "))
            print(f'{input} kilograms are equal to {input * pounds} pounds.')
            break
        
        elif option == 4:
            input = int(input("Input the miles number: "))
            print(f'{input} miles are equal to {input / pounds} kilos.')
            break
        
        ###########################################
        
        ##### START OF FERENHEIT - CELCIUS CONVERSION #####
        elif option == 5:
            input = int(input("Input the celcius temperature: "))
            print(f'{input} celcius are equal to {round(input * 1.8 + 32,2)} ferenheits.')
            break
        
        elif option == 6:
            input = int(input("Input the ferenheit temperatue: "))
            print(f'{input} ferenheits are equal to {round((input - 32) / 1.8,2)} celcius.')
            break
        ###########################################
        
        ##### START OF LITERS - GALOONS CONVERSION #####  
        elif option == 7:
            input = int(input("Input the number of liters: "))
            print(f'{input} listers are equal to {round(input * 0.2642,2)} gallons.')
            break
        
        elif option == 8:
            input = int(input("Input the number of gallons: "))
            print(f'{input} gallons are equal to {round(input / 0.2642,2)} liters.')
            break
        ###########################################   

        ##### START OF KW - HP CONVERSION #####  
        elif option == 9:
            input = int(input("Input the number of KW: "))
            print(f'{input} KWs are equal to {round(input * 1.3596,2)} horse powers.')
            break
        
        elif option == 10:
            input = int(input("Input the number HP: "))
            print(f'{input} HP are equal to {round(input / 1.3596,2)} kilowatts.')
            break
        

        else:
            print("Number of range, please input the  number 1-10")
            answer = input("Input 'y' if you with to continue or 'n' to cancel. ")
            if answer == 'n':
                print("Thank you! Bye, bye.")
                break
            elif answer == 'y':
                pass
            else: 
                print("\n ############## Invalid input. ##############\n")
                play == 'y'
        
'''
print('END OF GAME ON YOUR DEMOND!')
        