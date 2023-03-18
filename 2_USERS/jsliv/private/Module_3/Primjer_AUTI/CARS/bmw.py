class Bmw:
    def __init__(self):
        self.models = ["i8", "i10", "3", "5"]
        
    def ispis(self):
        print("Nisan - models: ")
        for model in self.models:
            print(model)
            
print(__name__)