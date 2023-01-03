car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

#x = car.values()
#print(x)
#car["year"] = 2018
#x = car.values()
#print(x)

car.update({"year": 2020})
car["wheel"] = 19
print(car, '\n\n')

for x, y in car.items():
  print(x, y)

auto = car.copy()

print(auto)