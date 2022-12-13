salary = float(input("Please input your montly salary: "))
years_in_service = float(input('Please input the years in service: '))

if years_in_service > 5:
    print('Total salary: ',(salary * 0.05))
else:
    print("No increase this year.")
    