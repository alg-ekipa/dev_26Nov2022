class Nissan:
    def __init__ (self):
        self.models = ['qashqai', 'R32', 'R34', 'R55']

    def ispis (self):
        print ('Nissan - models')
        for model in self.models:
            print (model)