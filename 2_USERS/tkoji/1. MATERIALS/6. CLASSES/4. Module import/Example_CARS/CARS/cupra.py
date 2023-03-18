
class Cupra:
    def __init__(self):
        self.models = ['FORMENTOR']


    def print_method(self):
        ''' Ovo je neka varjabala '''
        print('\Cupra - models:')
        for model in self.models:
            print(model, end=" ")

print(__name__)
