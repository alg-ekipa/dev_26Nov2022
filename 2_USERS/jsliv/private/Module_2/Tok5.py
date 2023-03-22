"""
income = 50000

if income < 10000:
    print("You don't have to pay tax.")
elif income < 20000:
    tax = income *0.2
    print(f"You have to pay {tax} US dollars.")
elif income < 40000:
    tax = income * 0.3
    print(f"You have to pay {tax} US dollars.")
else:
    tax = income * 0.4
    print(f"You have to pay {tax} US dollars.")
"""


list1 = [10,20,30,40,50]

new_list = reversed(list1)

for item in new_list:
    print(item)
