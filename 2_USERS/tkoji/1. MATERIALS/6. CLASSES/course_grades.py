
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
        
s1 = Student("San", 19, 95)
s2 = Student("Tom", 20, 99)
s3 = Student("Tim", 19, 65)

course = Course("Python", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

# Inheritence
print(course.students[0].name)
print(course.students[0].age)
        