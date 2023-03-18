class BMW:
    def __init__(self):
        self.models = ['i8', 'x5', 'x3', 'm3']

    def ispis(self):
        print ('BMW - models:')
        for model in self.models:
            print (model, end=' ')