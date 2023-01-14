#play = input("Do you wish to play? Enter y or n. ")
play = 'y'
miles = 0.6214
pounds = 2.2046

while play == 'y':
    option = int(input('''Please enter the number for desired conversion: 
        \n1. Kilometers to miles.
        \n2. Miles to kilometers.
        \n3. Kilogram to pounds.
        \n4. Pounds to kilograms.
        \nYour input here: '''))
    if option == 1:
        input = int(input("Input the km number: "))
        print(f'{input} km are equal to {input * miles} miles.')
        break
    elif option == 2:
        input = int(input("Input the miles number: "))
        print(f'{input} miles are equal to {input / miles} miles.')
        break
    
    elif option == 3: 
        input = int(input("Input the kg number: "))
        print(f'{input} kilograms are equal to {input * pounds} pounds.')
        break
    
    elif option == 4:
        input = int(input("Input the miles number: "))
        print(f'{input} miles are equal to {input / pounds} kilos.')
        break
    
    elif option == 5:
        input = int(input("Input the miles number: "))
        print(f'{input} miles are equal to {input / miles} miles.')
        break
    
    elif option == 6:
        input = int(input("Input the miles number: "))
        print(f'{input} miles are equal to {input / miles} miles.')
        break
    
    elif option == 7:
        input = int(input("Input the miles number: "))
        print(f'{input} miles are equal to {input / miles} miles.')
        break
# TODO 
    else:
        break