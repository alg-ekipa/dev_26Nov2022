from math import sqrt

triangle_side = float(input("Input the number. "))

def triangle_surface(num):
    ''' Function for Triangle surface '''
    
    P = num**2 * sqrt(3) / 4
    return P 

def triangle_h(num):
    v = num * sqrt(3) / 2
    return v


# Prints the docs for a function
print(triangle_surface.__doc__)
print()
print(triangle_surface.__name__)

print(triangle_surface(triangle_side))
print(triangle_h(triangle_side))