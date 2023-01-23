
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
    print("{:3}. {}".format(k,v))
    
change = int(input("\nWhich type of conversion you want to do. Choose 1 - 7"))

if change == 1:
    print("Choose type of the distance.")
    length_dict = \
        {
            1 : 'Kilometers'
            2 : 'Miles'
        }