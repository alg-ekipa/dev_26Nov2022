dummy_list = ["apple", "banana", "cherry"]
### Generate intial list 
numbers = list(range(1,6))
print("\n1st - Inital lists:\n", numbers, "\n", dummy_list)

# copy list using =
new_list = dummy_list
new_list.append('a')

# If we copy one list to another it does not copy the listm but only do a reference.
print('New List:', new_list)


