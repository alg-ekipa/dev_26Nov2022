
number_list = [1,2,4,4,5,7,8]

def sumNumbersInList():
    total = sum(number_list)
    return total

print(sumNumbersInList())

def multiplyNumbers(num_values):
    total = 1
    for i in num_values:
        total *= i
    return total

print(multiplyNumbers((2,5,1,1)))