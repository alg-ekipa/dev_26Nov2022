
# TODO - in progress
unit_options = \
    {
        1: "Distance",
        2: "Temperature",
        3: "Weight",
        4: "Voulume",
        5: "Power",
    }

for k,v in unit_options.items():
    print("{:3}: {}".format(k,v))
    
change = int(input("\nWhich type of conversion you want to do. Choose 1 - 7. "))

if change == 1:
    length_dict = \
        {
            1 : 'Kilometers',
            2 : 'Miles'
        }
    for k,v in length_dict.items():
        print("{:3}: {}".format(k,v))
        
    option = int(input("\nWhich type of conversion you want to do. Choose 1 - 2. "))
            
    if option == 1:
        print("Option 1.")
        conversion = int(input("Input kilometer number: "))
        # TODO - dummy input, demonstration math only.
        print(f'{ conversion } km are equal to { conversion * 123.123 } miles.')
    elif option == 2:
        print("Option 2.")
        conversion = int(input("Input miles number: "))
        # TODO - dummy input, demonstration math only.
        print(f'{ conversion } miles are equal to { conversion / 123.123 } kilometers.')
    else:
        print("Incorrect input")
        