class Bmw:
    def __init__(self):
        self.models=['i8', 'x1', 'x5', 'x7']
        
    def ispis(self):
        print('BMW - models: ')
        for model in self.models:
            print(model)
        print()
print(__name__)

