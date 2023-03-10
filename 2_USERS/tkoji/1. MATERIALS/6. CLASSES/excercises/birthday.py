# ZADATAK
# kreirati klasu korisnika, svojstva po izboru, no mora imati datum rodenja, ime i prezime je jedna varijabal koja se razdvoji na dvije 
# u klasi definirati metodu kojom se se racuna staros korisnika da se oduzme danasnji datum od njegovo datuma rodenja.
# koristiti module datetime
# kreirti par objekata i pozivati metodu i ispisati starost korisnika

from datetime import datetime
now = datetime.now().strftime('%d.%m.%Y')

class Person():
    def __init__(self, name, birthday, sex):
        self.name = name
        self.birthday = birthday
        self.sex = sex
        
    def name_surname(self):
        result = self.name.split(" ")
        name = result[0]
        surname = result[1]
        print(f'\nName: {name}\nSurname: {surname}')

    def convert_date(self, date_of_birth):
        date_of_birth = datetime.strptime(date_of_birth, '%d.%m.%Y')
        date_of_birth = datetime.strftime(date_of_birth, '%d.%m.%Y')
        print(date_of_birth)
        
    def calculate_age(self, date):
        real_date = self.convert_date(date)
        today = now
        print(today)
        age = today - real_date
        print(age)

    def print_persons(self):
        print(self.name)

list_of_friends = []

name_surname = "Harry Potter"
birthday = '9.4.2001'
sex = 'wizard'

person1 = Person(name_surname, birthday, sex)
person1.name_surname()
person1.convert_date(birthday)
person1.calculate_age(birthday)







        
    



