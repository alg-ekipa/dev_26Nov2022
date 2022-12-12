""" User inputs """
car_consumption = float(input('\nEnter your average car consumption: '))
fuel_price = float(input('Add current petrol price: '))
avg_daily_milage = float(input('What is your average daily milage? '))
avg_days_per_month = float(input('How many days a month you drive your car? '))
print("\nPlase give us more information so we calculate more infromation for you.\n")
car_tank_size = float(input('What is the car tank size? '))
car_total_milage = float(input('What is the total car milage? '))
print("\nThank you! Here are you statistics.\n")

""" Calculated fields """
fuel_price_per_km = round((fuel_price * car_consumption) / 100,3)
fuel_cost_per_month = round((avg_daily_milage * fuel_price_per_km ) * avg_days_per_month,2)
fuel_total_liters_per_month = fuel_cost_per_month / fuel_price
fuel_refill_times = fuel_total_liters_per_month //  fuel_total_liters_per_month
#TODO - wrong calculation
#fuel_price_surge = round(((23 / fuel_price)* 100 ) * avg_daily_milage * avg_days_per_month,2)
fuel_total_money_spent = round(car_total_milage * fuel_price_per_km,2)

""" User outputs """
print(f'Total cost of fuel per month: {fuel_cost_per_month}HRK')
print(f'You car consumption per kilometer is ~{fuel_price_per_km}HRK')
print(f'With an average consumption of {car_consumption} you will need to refill you car {fuel_refill_times} per month.')
#TODO - wrong calculation
# print(f'If fuel price surges for 23% your montly expense for the fuel will be {fuel_price_surge}HRK')
print(f'For the total milage of \'{car_total_milage}\' you spent {fuel_total_money_spent}HRK.')