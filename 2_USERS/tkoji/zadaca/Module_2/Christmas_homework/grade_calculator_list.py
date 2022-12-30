
grade_list = []
counter = 0

student_number = int(input('How many students are in the class? '))


while True:
    if counter >= student_number:
        print(f"Student{counter} was the last student.")
        break
    for i in range(0, student_number):
        counter += 1
        grades = int(input(f"Add grade 1-5 for Student{counter}: "))

        if grades in range(0,6):
            grade_list.append(grades)
        elif grades not in range(0,6):
            print("Please input a number in the range from 1 to 5.")
            counter -= 1
        if counter >= student_number:
            break

fives = grade_list.count(5)
ones = grade_list.count(1)

print(f"There are {counter} students in the this class and the average grade is {round(sum(grade_list) / student_number,2)}")

if fives == 1:
    print("Only one student has grade 5.")
else:
    print(f"There are ('{fives}') 5 grades in the among the class of {student_number}") 
    
if ones == 1:
    print("Only one student has grade 1.")
else:
    print(f"There are ('{ones}') 1 grades in the among the class of {student_number}") 


