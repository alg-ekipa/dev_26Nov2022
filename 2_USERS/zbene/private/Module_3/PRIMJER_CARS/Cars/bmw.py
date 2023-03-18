class Bmw:
    def __init__ (self):
        self.models = ['i8', 'x1', 'x5', 'x6']

    def ispis (self):
        print ('Bmw - models')
        for model in self.models:
            print (model)