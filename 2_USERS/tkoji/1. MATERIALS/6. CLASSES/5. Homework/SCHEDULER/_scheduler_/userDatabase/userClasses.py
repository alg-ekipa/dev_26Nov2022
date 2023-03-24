print("Hello from the other side.")

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
         
    def get_task(self):
        return self.task
    
class DateTimeManager:
    def __init__(self, event_date):
        self.event_date = event_date
        
    def format_time(self):
        d = datetime.strptime(self.event_date, '%d.%m.%Y %H:%M:%S')
        d_format = d.strftime('%d.%m.%Y %H:%M:%S')
        return d_format