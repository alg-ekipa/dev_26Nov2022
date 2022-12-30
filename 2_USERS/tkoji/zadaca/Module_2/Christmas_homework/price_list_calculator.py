
price_list = []
counter = 0
articles = int(input('For how many articles you want to add the price? '))

while True:
    if counter >= articles:
        print(f"No more prices to add. Exiting program...")
        break
    for i in range(0, articles):
        counter += 1
        price_input = [float(price) for price in input("Enter the list of prices : ").split()]
        price_list.append(price_input)
    
price_max = (max(price_list))
price_max = price_max[0]
price_min = (min(price_list))
price_min = price_min[0]

price_diff = price_max - price_min

print(f"There are {counter} article prices in the list, the difference between minumal and maximal is {price_diff}.")
