keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

number_dict = dict()

for i in range(len(keys)):
    number_dict.update({keys[i]: values[i]})
    print(number_dict)