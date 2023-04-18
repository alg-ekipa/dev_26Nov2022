class Vehicle():
      def __init__(self, type, model, plate, year, price):
            self.type = type
            self.model = model
            self.plate = plate
            self.year = year
            self.price = price
        
      def print_vehicle(self):
            print (f'\n\nType: {self.type}\nModel: {self.model}\nProduced: {self.year}\nMarket price: {self.price}')
      
      def delivery_vehicle(self):
            if self.type == "Dostavno vozilo":
                  print(self.model)
      
      def vehicle_year(self):
            if self.year > 2015:
                  print(f'Car {self.model} is not older than 8 years.')
       
       
      def plates(self, car_plate):
            if car_plate == self.plate:
                  self.print_vehicle()
      
car_databases = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00],
}

car_list = []

for i in car_databases.values():
      t = i[0]
      m = i[1]
      p = i[2]
      y =  i[3]
      pr = i[4]
      vehicle_object = Vehicle(t,m,p,y,pr)
      car_list.append(vehicle_object)
      #vehicle_object.print_vehicle()


# for i in car_list:
#   i.delivery_vehicle()
  
for i in car_list:
      i.vehicle_year()

plates = input('\nPlease enter your car plate number:')
for i in car_list:
    i.plates(plates)
  
  