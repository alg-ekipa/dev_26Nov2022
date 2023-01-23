dummy_list = ["apple", "banana", "cherry"]
### Generate intial list 
numbers = list(range(1,11,2))
print("\n1st - ", numbers)

# index method tells a numberic position of an element in the list 
num = numbers.index(9)
print(num)

fruit = dummy_list.index("banana")
print(fruit)

# insert method inserts the element on specified position without removing the current value,
# but move it one position ahead
print(dummy_list)
dummy_list.insert(1, "jabuka")
print(dummy_list)
dummy_list.insert(3, "jabuka")
print(dummy_list)



