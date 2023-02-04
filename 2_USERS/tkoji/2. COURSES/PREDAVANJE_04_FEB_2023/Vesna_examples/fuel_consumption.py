

fuel_price = 1.53
price_limit = 0.27 * 100

def gas_price_per_hounderd_km(liters):
    total_price = liters * fuel_price
    return total_price

car_consumption = int(input('Input car consumption in liters per 100km: '))
total_price = gas_price_per_hounderd_km(car_consumption)

print(total_price)

if gas_price_per_hounderd_km(total_price) < price_limit:
    print("Suitable choice")
else:
    print("Car is to expenisve.")
