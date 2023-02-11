eggs = 11

def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    print(eggs)
    
spam()