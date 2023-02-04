
# no arguments
def ola():
    print("Ola Maria!")
    

# two argumets
def olaaa(name, surname):
    print(f'Hello, {name} {surname}')
    
# single argument with return
def get_ola(name):
    return f'Hello, {name}'

# print each
greeting = get_ola('Pythonac.')
print(greeting)
print(get_ola('Tom'))


# two arbitrary arguments
def mat(num, num_inc):
    return num + num_inc
print(mat(4,10))

# two arguments, one fixed
def mat2(num, num_inc=10):
    return num + num_inc

print(mat2(10,11))