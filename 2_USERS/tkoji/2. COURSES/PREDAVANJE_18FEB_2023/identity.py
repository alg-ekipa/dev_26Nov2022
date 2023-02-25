
users = {
    "admin": ["admin","admin","superSecret"],
    "tom": ["Major ","Tom","1nitalP4ssworD"],
    "harry": ["Harry","Potter","gryffindor4life"]
}

def user_login(username,password):
    if username in users.keys() and (users[username][2] == password):
        print('Auth ok.')
        return True
    else:
        print('Auth not ok.')
        return False
    
def user_db_inspection(user):
    if user not in users.keys():
        return True
    else:
        return False

def user_add():
    user_add = str(input("Please input the username."))
    if user_db_inspection(user_add) == True:
        user_first_name = str(input("Enter user's first name. "))
        user_last_name = str(input("Enter user's last name."))
        user_password = str(input("Enter user's password."))
        user_definitons = [user_first_name] + [user_last_name] + [user_password]
        print(user_definitons)
        users[user_add]=user_definitons
        print(users)            
    else:
        print("User already in the database. Please try with a differnet username.")

def user_del(username):
    if username in users:
        del users[username]
    print("Username: ", username, " has been deleted from a database.")

def user_mod():
    menu_loop_control = True
    while menu_loop_control:
        username = input("Please enter the username you wish to edit. ")
        if username in users.keys():
            sub_menu_loop_control = True
            while sub_menu_loop_control:
                choice_user = input('''\nWhat would you like to change.
                    1) First Name
                    2) Last Name
                    3) Password
                    4) Or 'q' to quit.\nInput: ''')
                if choice_user.isdigit():
                    choice_user = int(choice_user)
                if choice_user == 1:
                    firstName = input("Please choose a username you want the change the first name. ")
                    user_change_firstName(firstName)
                if choice_user == 2:
                    lastName = input("Please choose a username you want the change the last name. ")
                    user_change_lastName(lastName)
                if choice_user == 3:
                    new_userPassword = input("Please choose a username you want the change the password? ")
                    user_change_password(new_userPassword)
                if choice_user == 'q' or choice_user == 'Q' or choice_user == 'quit':
                    sub_menu_loop_control = False
                    menu_loop_control = False
                    break
                else:
                    print("Incorrect choice.")
                    choice = input("Do you wish to try again? ( yes / no )? ").lower()
                    if choice == 'y' or choice == 'yes':
                        break
                    elif choice == 'n' or choice == 'no':
                        menu_loop_control = False
                        break
                    else:
                        print("Incorrect choice. Please enter 'yes' or 'no'.")

        else:
            print("User not in the database.")
            choice = input("Username not in the database. Do you wish to continue ( yes / no )? ").lower()
            if choice == 'y' or choice == 'yes':
                enu_loop_control = True
            elif choice == 'n' or choice == 'no':
                menu_loop_control = False
                break
            else:
                print("Incorrect choice. Please enter 'yes' or 'no'.")
        
def user_change_password(username):
    if username in users:
        while True:
            new_password = input(f"Changing password for user: {username}. Set the new password (must be at least 10 characters long): ")
            if len(new_password) >= 10:
                users[username][2] = new_password
                print(f"Password updated for user {username}.")
                break
            else:
                print("Password must be at least 10 characters long.")
    else:
        print(f"User {username} not found in the database.")

def user_change_firstName(username):
    if username in users:
        while True:
            new_firstName = input(f"Changing first name for user: {username}. Update: ")
            users[username][0] = new_firstName
            print(f"First name updated for: {username}.")
            break
    else:
        print(f"User {username} not found in the database.")

def user_change_lastName(username):
    if username in users:
        while True:
            new_lastName = input(f"Changing last for user: {username}. Update:  ")
            users[username][1] = new_lastName
            print(f"Last name updated for: {username}.")
            break
    else:
        print(f"User {username} not found in the database.")


     
main_menu = True
while main_menu == True:
    print(
        '''     Hello, welcome to ALG-EKIPA access and indentity management.
        Please authenticate to start using the system or type 'q' to quit.\n ''')
    username = input("Please enter the username: ")
    password = input("Please enter the password: ")

    if user_login(username,password) == True:
        if username == 'admin':
            admin_choice = print('''Welcome to an administator account. Please choose what would you like to do?
                \t\t 
                1) Add new user
                2) Change existing user first name
                3) Change existing user last name
                4) Change existing user password.
                5) Logout.''')
            if admin_choice == 1:
                pass
            if admin_choice == 2:
                pass
            if admin_choice == 3:
                pass                
            if admin_choice == 4:
                pass
            if admin_choice == 5:
                pass
            else:
                pass
            
    #     if username != 'admin':
    # else:
    #     print("Authentication failed.")
    #     choice = input('Do you wish try again? (yes/no) ')
    #     if choice == 'y' or choice == 'yes':
    #         main_menu = True
    #     elif choice == 'n' or choice == 'no':
    #         main_menu = False
    #         break
    #     else:
    #         print("Incorrect choice. Please enter 'yes' or 'no'.")



