
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
        
tom_serial_car = Car("Cupra","Formentor")
print(f'Tom\'s serial car is {tom_serial_car.manuf}:{tom_serial_car.model} in {tom_serial_car.color} color with sport mode: {tom_serial_car.sport}')

tom_serial_car.change_color_red('black')
print(f'Tom\'s new car is {tom_serial_car.manuf}:{tom_serial_car.model} in {tom_serial_car.color} color with sport mode: {tom_serial_car.sport}')

tom_serial_car.sport_mode()
print(f'Tom decided to tune the and new car is {tom_serial_car.manuf}:{tom_serial_car.model} in {tom_serial_car.color} color with sport mode: {tom_serial_car.sport}')