

class Users:
    def __init__(self, name:str):
        self.name = name 
            
    def add_user(self):
        print(self.name)

    def get_name(self):
        result = self.name.split(" ")
        client_name = result[0]
        return client_name
        
    def get_surname(self):
        result = self.name.split(" ")
        client_surname = result[1]
        return client_surname
       
        

#user_object = users.Users.add_user(user1)
#user_database_list.append(user_object)

#print(user_database_list)

user_database_list = []
user1 = 'Tomi TOm'


a = Users(user1)
print(a.get_name())
