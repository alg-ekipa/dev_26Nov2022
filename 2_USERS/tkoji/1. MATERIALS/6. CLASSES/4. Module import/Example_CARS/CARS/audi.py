
class Audi:
    def __init__(self):
        self.models = ['A6', 'Q7','A8']


    def print_method(self):
        ''' Ovo je neka varjabala '''
        print('\nAudi - models:')
        for model in self.models:
            print(model, end=" ")
            

print(__name__)
