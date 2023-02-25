from re import S


class Student:
    def __init__(self, name, sname, grade):
        self.name = name
        self.sname = sname
        self.grade = grade
        
    def print_class(self):
        print(f'Student: {self.name} {self.sname}, ocjena: {self.grade}')
        
    def print_grade_e(self):
        if self.grade == 1:
            self.print_class()
        else:
            print("No bad grades.")

student_object_list = []
        
for i in range(3):
    input_name = input("Name: ")
    input_sname = input("Sname: ")
    input_grade = int(input("Grade: "))
    
    student_object = Student(input_name, input_sname, input_grade)

    student_object_list.append(student_object)

# for i in student_object_list:
#     i.print_class()

#TODO ispis ne radi, treba popraviti.
for i in student_object_list:
    i.print_grade_e()