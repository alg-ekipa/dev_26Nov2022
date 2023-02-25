class MyTvDevice():
    ''' A class that describes a TV device'''
    
    def __init__(self, model, manuf, size, turn_on=False, programs=0, volume=0):
        self.model = model
        self.manuf = manuf
        self.size = size
        self.trunOn = turn_on
        self.programs = programs
        self.volume = volume
        
    def turn_on(self):
        self.trunOn = True
        self.programs = 1
        self.volume = 3
        
    def change_program(self, channel):
        self.programs = channel
        
    def change_volume(self, volume):
        self.volume = volume
        

living_room_tv = MyTvDevice("A1","TCL", 65)
print(living_room_tv.model)
living_room_tv.turn_on()
print(f'A TV in the living room is: {living_room_tv.model}.')
living_room_tv.change_volume(100)
print(f'A TV in the living room is: {living_room_tv.model} and volume is set to "{living_room_tv.volume}"')
living_room_tv.change_program(11)
print(f'A TV in the living room is: {living_room_tv.model}, volume is set to "{living_room_tv.volume}" and you are watching channel number "{living_room_tv.programs}".')

office_tv = MyTvDevice("Model 1", "Sony", 55)
kitchen_tv = MyTvDevice("HDR", "LG", 66)

tv_list = (living_room_tv.manuf, office_tv.manuf, kitchen_tv.manuf)
print(tv_list) 



