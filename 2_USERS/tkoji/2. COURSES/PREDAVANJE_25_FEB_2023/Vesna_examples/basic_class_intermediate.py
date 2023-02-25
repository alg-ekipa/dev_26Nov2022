from pkg_resources import IMetadataProvider


class Student():

    # KONSTRUKTOR je metoda koje se zove __init__ (initialization), u nju se prensose parametri odnosno karakteristike (svojstva) eng, property
    # prvi argument je uvijek SELF
    def __init__(self, name, sname, oib, grade):
        # definiramo da se pridruzivanje vrijednosti uvijek odnosi na objekt koji inicijaliziramo
        self.name = name
        self.sname = sname
        self.oib = oib
        self.grade = grade
     
    # A method that prints the values   
    def print_properties(self):
        print(self.name, self.sname, self.oib, self.grade)
       
def avg(list):
    return sum(list) / len(list)

student1 = Student('Marko','Now',666, 1)
student2 = Student('John', 'Doe',123,5)

student_list = [student1.name, student1.sname, student2.name, student2.sname]
print(student_list)


name_student3 = input("Name: ")
sname_student3 = input("Sname: ")
oib_student3 = input("OIB: ")
grade_student3 = int(input("grade: "))

student3 = Student(name_student3, sname_student3, oib_student3, grade_student3 )
student_list = [student1.name, student1.sname, student2.name, student2.sname,  student3.name, student3.sname ]
print(student_list)


grade_list = [student1.grade, student2.grade, student3.grade]
print(f'An average grade for these students is: { round(avg(grade_list),2)}')

student1.print_properties()


# TODO 
# napraviti kreiranje objekata kroz petlju
# pet ucenika, krerajte kao objete klase ucenik
