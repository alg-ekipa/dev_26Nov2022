class BMW:
    def __init__(self):
        self.models=['X5','X6','X7','M3']

    def ispis(self):
        print('BMW - models: ')
        for model in self.models:
            print(model)

print(__name__)