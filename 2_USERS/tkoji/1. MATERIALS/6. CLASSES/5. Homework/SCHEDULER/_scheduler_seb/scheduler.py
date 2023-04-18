from userClasses import User, Task

user_database =  []

def init_database(user: User, task: Task):
    user.add_task(task)
    if user not in user_database:
        user_database.append(user)
        
def print_scheduler():
    for u in user_database:
        u.print_tasks()

#Main program
while True:
    user_name = input("Please enter your nickname: ").capitalize()
    user_task = input("What task you with to add to the list? ").capitalize()
    user_time = input("At what time? (mm.dd.yyyy HH:mm:ss) ")

    user = User(user_name)
    task = Task(user_task, user_time)
    
    init_database(user, task)
    
    while True:
        user_choice = input("Do you wish to add another task? (yes/no) ")
        if user_choice == 'yes' or user_choice == 'y':
            user_task = input("What task you wish to add to the list? ")
            user_time = input("At what time? ")       
            
            task = Task(user_task, user_time)
            init_database(user, task)
            
        else: 
            break
    
    user_choice = input("Do you wish to add another user: (y/n) ")
    if user_choice not in ["y","yes"]:
        break        
        

print_scheduler()


