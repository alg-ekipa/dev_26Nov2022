
username = ''
password = ''
users = {
    "admin": ["admin","admin","superSecret"]
}
def user_login(user_auth,user_pass):
    if user_auth in users.keys() and (users[user_auth][2] == user_pass):
        return True
    else:
        return False
 
def user_db_inspection(user):
    if user not in users.keys():
        return True
    else:
        return False

def user_add():
    user_add = str(input("Please input the username."))
    print(user_add)
    if user_db_inspection(user_add) == True:
        user_first_name = str(input("Enter user's first name. "))
        user_last_name = str(input("Enter user's last name."))
        user_password = str(input("Enter user's password."))
        user_definitons = [user_first_name] + [user_last_name] + [user_password]
        print(user_definitons)
        users[user_add]=user_definitons
        print(users)
        
        

            
            
    else:
        print("Else")
        

def user_del():
    pass

user_add()