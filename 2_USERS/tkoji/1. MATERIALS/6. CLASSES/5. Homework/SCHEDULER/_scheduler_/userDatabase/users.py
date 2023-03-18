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
    
class dateTimeManager:
    def __init__(self, event_date):
        self.event_date = event_date
        
    def format_time(self):
        d = datetime.strptime(self.event_date, '%Y.%m.%d')
        d_format = d.strftime('%d.%m.%Y')
        return d_format

user_database: dict()

while True:
    user = input("Please enter your name and surname: ")
    user_task = input("What task you with to add to the list? ")
    user_time = input("At what time? ")

    user_object = Users(user,user_task)
    user_object_time = dateTimeManager(user_time)
    
    user_database.[user]=user_database
    
