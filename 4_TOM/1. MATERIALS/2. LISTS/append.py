dummy_list = ["apple", "banana", "cherry"]
### Generate intial list 
numbers = list(range(1,4))
print("\n1st - Inital list: ", numbers)

# Append to the list
numbers.append('aa')
print("2nd - string 'aa' appended: ", numbers)

# Append one list to another
numbers.append(dummy_list)
print("3rd - append one list to another: ", numbers)

# Append single value from one list to another
numbers.append(dummy_list[0])
print("4th - appends single value from one list to another: ", numbers)

