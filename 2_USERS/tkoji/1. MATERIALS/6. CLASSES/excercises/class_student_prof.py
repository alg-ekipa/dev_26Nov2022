# Class Osoba - parent
# Prof and student are childs
# input for students and profesors
# append to list

class Person:
    def __init__(self, name, surname, role):
        self.name = name
        self.surname = surname
        self.role = role
 
    def print_persons(self):
        print(f'Surname: {self.name}\n:Name: {self.name}.')

    class Professor:
        def __init__(self, name, surname, role, course, expirence):
            super().__init__(name, surname, role)
            self.course = course
            self.expirece = expirence
            
        def print_professor(self):
            if self.role == 'professor':
                print(f'Surname: {self.name}\n:Name: {self.name} is {self.role}')

    class Student:
        def __init__(self, name, surname, role, lecture, year):
            super().__init__(name, surname, role)
            self.lecture = lecture
            self.year = year

        def print_sudent(self):
            if self.role == 'student':
                print(f'Surname: {self.name}\n:Name: {self.name} is {self.role}')

list_students = []
list_professors = []

s1 = Student()

# TODO - homework

