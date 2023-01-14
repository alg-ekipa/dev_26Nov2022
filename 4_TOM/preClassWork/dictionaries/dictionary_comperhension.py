# Dictionary comprehension is an elegant and concise way to create dictionaries.
# Example, a for loop that builds multiplication table as a dict.

# an empty dict can be initiated in two ways, with curlies or dict() function.
square_dict = dict()
square_dict = {}

# 
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

