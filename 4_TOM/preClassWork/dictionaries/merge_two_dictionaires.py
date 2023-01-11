dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# **kwargs in function definition
#In the same way we can destructure lists with the asterisk (*) operator, we can use the double-asterisk (**) operator to destructure dictionaries in Python functions.

dict3 = {**dict1, **dict2}
print({**dict1})