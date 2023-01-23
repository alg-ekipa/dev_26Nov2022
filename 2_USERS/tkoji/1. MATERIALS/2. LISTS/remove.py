# remove()	Removes the first item with the specified value

### Generate intial list 
numbers = list(range(1,11))
print("\n1st - ", numbers)

# Second 9 appended
print(numbers)
numbers.append(9)
print(numbers)

# remove method removes only the first occurence
numbers.remove(9)
print(numbers)
