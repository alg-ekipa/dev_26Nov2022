class Audi:
    def __init__(self):
        self.models = ['a6', 'a8', 'a4', 'a3']

    def ispis(self):
        print ('Audi - models: ')
        for model in self.models:
            print(model)