from datetime import datetime
now = datetime.now().strftime('%d.%m.%Y')

class Users:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        
    def get_name(self):
        result = self.name.split(" ")
        user_name = result[0]
        return user_name
    
    def get_surname(self):
        result = self.name.split(" ")
        user_surname = result[1]
        return user_surname
     
    def get_task(self):
        return self.task
    
class DateTimeManager:
    def __init__(self, event_date):
        self.event_date = event_date
        
    def format_time(self):
        d = datetime.strptime(self.event_date, '%d.%m.%Y %H:%M:%S')
        d_format = d.strftime('%d.%m.%Y %H:%M:%S')
        return d_format

user_database =  dict()

def init_database(user,task, time):
    
    user_object = Users(user,task)
    username = user_object.get_name()
    usettask = user_object.get_task()
    
    user_object_time = DateTimeManager(time)
    user_fromat_time = user_object_time.format_time()
   
    if username not in user_database.keys():
        user_database[username] = []
    
    if username in user_database.keys():
        user_database[username].append([usettask,user_fromat_time])
    else:
        print("Something went wrong.")

def print_scheduler():
    print(f'\nHello {(list(user_database)[0])}, here is your plan.')
    print('_' * 30)

    for user, values in user_database.items():
        for lst in values:
            print(f'{lst[0]} \t@ {lst[1]}')

# Main program
main_menu = True
while main_menu == True:
    user = input("Please enter your nickname: ")
    user_task = input("What task you with to add to the list? ")
    user_time = input("At what time? (mm.dd.yyyy HH:mm:ss) ")

    init_database(user,user_task, user_time)
    
    sub_menu = True
    while sub_menu == True:
        user_choice = input("Do you wish to add another task? (yes/no) ")
        if user_choice == 'yes' or user_choice == 'y':
            user_task = input("What task you wish to add to the list? ")
            user_time = input("At what time? ")         
            init_database(user,user_task, user_time)
        else: 
            sub_menu == False
            break
 
    break

print_scheduler()