class Bmw:
    def __init__(self):
        self.models =['3-er','5-er','X5','X7']
    
    def ispis(self):
        print('BMW - models:')
        for model in self.models:
            print(model)

print(__name__)