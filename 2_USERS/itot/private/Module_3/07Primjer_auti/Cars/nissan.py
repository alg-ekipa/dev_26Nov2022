class Nissan:
    def __init__(self):
        self.models = ['qashqai', 'Skyline', 'Micra', 'Note']

    def ispis(self):
        print ('Nissan - models: ')
        for model in self.models:
            print(model)