class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []
                
    def add_task(self, task):
        self.tasks.append(task)
                
    def get_name(self):
        result = self.name.split(" ")
        user_name = result[0]
        return user_name
         
    def get_task(self, task_name): 
        for i in self.tasks:
            if i.name == task_name:
                return i
        return None
    
    def print_tasks(self):
        print(f'Tasks for user {self.name}: ')        
        for t in self.tasks:
            print(t)
        
        
    @classmethod
    def info(cls):
        pass
    # management metode, find users with the same task - parameters: list  + user task name
      
from date_time_manager import DateTimeManager

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
               
    def __str__(self) -> str:
        return f'S1: This task: {self.name} at {DateTimeManager.format_time(self.deadline)}'
    

# # instance klase user.    
# user1 = User("Tom")
# task1 = Task("Ovo", "1000.12.21 10:00:00")
# print(task1)

# user1.add_task(task1)
# print(user1.get_task("Ovo"))

# user2 = User("Seb")
# user2.add_task(task1)
# print(user2.get_task("Ovo"))