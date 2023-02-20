name1 = "YK"
height1 = 2
weight1 = 90

name2 = "YK's sister"
height2 = 1.8
weight2 = 70

name3 = "YK's brother"
height3 = 2.5
weight3 = 160

def bmi_calculator(name,height, weight):
    bmi = round(weight / (height **2), 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height1, weight1)
result2 = bmi_calculator(name2, height2, weight2)
result3 = bmi_calculator(name3, height3, weight3)

print(result1)
print(result2)
print(result3)