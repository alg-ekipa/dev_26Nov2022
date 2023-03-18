class Audi:
    def __init__(self):
        self.models=['a6','q7','a3','a8']

    def ispis(self):
        print('Audi - models: ')
        for model in self.models:
            print(model)

print(__name__)