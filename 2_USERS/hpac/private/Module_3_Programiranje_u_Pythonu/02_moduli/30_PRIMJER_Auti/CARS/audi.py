class Audi:
    def __init__(self):
        self.models =['A4', 'A6','Q7','A8']
    
    def ispis(self):
        print('Audi - models:')
        for model in self.models:
            print(model)

print(__name__)