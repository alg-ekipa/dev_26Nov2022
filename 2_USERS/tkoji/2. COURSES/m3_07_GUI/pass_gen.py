import random as rd

# numbers = 48 - 57
# letters = 65 - 90, 97 - 122


def generate_password(user_choice):
    passwd = str('')
    password_lenght = int(input("Enter length: "))
    user_choice = int(input("Enter choice: "))


    for i in range(password_lenght):
        if user_choice == 1:
            a = rd.choice([(65,89),(97,122)])
        elif user_choice == 2:
            a = rd.choice([(48,57)])
        elif user_choice == 2:
            a = rd.choice([(33,47),(57,64),(91,96)])
            
    number = rd.randint(*a)
    charcater = chr(number)
    passwd += charcater
    return passwd

izbor = int(input("Choose: "))
print(generate_password(izbor))




                                     
                                     