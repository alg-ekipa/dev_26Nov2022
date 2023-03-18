class Audi:
    def __init__(self):
        self.models = ["A1", "A3", "Q3", "Q5"]
        
    def ispis(self):
        print("Audi - models: ")
        for model in self.models:
            print(model)
            
print(__name__)