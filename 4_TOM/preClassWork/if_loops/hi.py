# Test simple condition
number = 6
if number > 9:
    # Calculate square
    print(number * number)
    print('1st line of comment')
else:
    # Calculate distance
    print (number * number * 11)
    print("2nd line of comment.")
    
#
# Evaluate input
# 
password = input('Please input the password: ')

if password == "Password123":
    print("Ha! That was easy!")
else:
    print('Incorrect password!')
