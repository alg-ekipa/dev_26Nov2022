class Car():
    ''' A class that describes the car'''
    def __init__(self, manuf, model, color='gray', sport_suspension=False):
        self.manuf = manuf
        self.model = model
        self.color = color
        self.sport = sport_suspension
    
    def change_color_red(self, new_color):
        self.color = str(new_color)
        
    def sport_mode(self):
        self.sport = True
        
    def car_properties(self):
        print(self.manuf, self.model, self.color,self.sport)
   
# Inicirajte 3 objekta
# spremite ta 3 objekta u listu: car_object_list
# dodajte u klasi methodu za ispis samo crvenih auta i pozovite ju 

