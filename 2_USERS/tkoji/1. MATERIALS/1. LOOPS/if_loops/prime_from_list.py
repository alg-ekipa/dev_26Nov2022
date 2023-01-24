import random

randomlist = random.sample(range(1, 31), 30)
randomlist.sort()

divisible_list_3 = []
divisible_list_5 = []
not_divisible = []

for i in randomlist:
    if i % 3 == 0:
      if i % 5 == 0:
        divisible_list_3.append(i)
        divisible_list_5.append(i)
      else:
        divisible_list_3.append(i)
    elif i % 5 == 0:
        divisible_list_5.append(i)
    else:
        not_divisible.append(i)
       
print("Not divisible:\t", not_divisible) 
print("List of numbers divisible by 3:\t", divisible_list_3)
print("List of numbers divisible by 5:\t", divisible_list_5)
