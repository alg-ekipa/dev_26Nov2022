
class Dog:
    
    def __init__(self, name):
        self.name = name
        print(name)
        
    
    def bark(self):
        print("bark!")
        
    def meow(self):
        return "meow"
    
    
d = Dog('Tom')
d.name
d.bark()
print(d.meow())