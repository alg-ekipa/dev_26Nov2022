name1 = "YK"
height = 2
weight = 90

name2 = "YK's sister"
height = 1.8
weight = 70

name3 = "YK's brother"
height = 2.5
weight = 160

def bmi_calculator(name,height, weight):
    bmi = weight / (height **2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height, weight)
result2 = bmi_calculator(name2, height, weight)
result3 = bmi_calculator(name3, height, weight)

print(result1)
print(result2)
print(result3)