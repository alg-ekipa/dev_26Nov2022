class Nissan:
    def __init__(self):
        self.models = ['quasqua', 'gtr', 'r34', 'r55']

    def ispis(self):
        print ('Nissan - models:')
        for model in self.models:
            print (model, end=' ')