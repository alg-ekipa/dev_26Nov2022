# the list.extend() method is used to iterate over an iterable (string, tuple, list, set, or dictionary)]
# and then add each element of the iterable to the end of the current list. The length of the list increases 
# by the number of elements present in the iterable.

dummy_list = ["apple", "banana", "cherry"]
### Generate intial list 
numbers = list(range(1,11,2))
print("\n1st - ", numbers)

# It not that another list becomes a nasted list, but it appends items.
dummy_list.extend(numbers)
print("2nd -", dummy_list)

numbers.append(dummy_list)
print("3rd - ",numbers)
