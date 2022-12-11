#fuel_price = 9.53
#car_consumption = 5.3
#avg_daily_milage = 40
#avg_days_per_month = 30

car_consumption = float(input('\nEnter your average car consumption: '))
fuel_price = float(input('\nAdd current petrol price: '))
avg_daily_milage = float(input('\nWhat is your average daily milage? '))
avg_days_per_month = float(input('\nHow many days a month you drive your car? '))

fuel_price_per_km = round((fuel_price * car_consumption) / 100,3)
print(f'You car consumption per kilometer is ~{fuel_price_per_km}HRK')

fuel_cost_per_month = (avg_daily_milage * fuel_price_per_km ) * avg_days_per_month 
print(f'Total cost of fuel per month: {fuel_cost_per_month}HRK')

#TODO
# - what is the car tank size?
# - based on consumption how many times a month a client will need to refill his car
# - what will be the client montly cost if the petrol price surges for 23%
# - what is the total car milage?
# - how much money in total client spent driving that car?
