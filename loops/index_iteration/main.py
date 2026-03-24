prices = [29.99, 45.50, 12.75, 38.20]
for price in range(len(prices)):
    if price == 0:
        discount_factor=0.1
        prices[price] -=prices[price] * discount_factor
        print(f"Updated price for item {price} : ${prices[price]:.2f}" )
    if price == 1:
        discount_factor=0.2
        prices[price] -=prices[price] * discount_factor
        print(f"Updated price for item {price} : ${prices[price]:.2f}" )
    if price == 2:
        discount_factor=0.15
        prices[price] -=prices[price] * discount_factor
        print(f"Updated price for item {price} : ${prices[price]:.2f}" )
    if price == 3:
        discount_factor=0.05
        prices[price] -=prices[price] * discount_factor
        print(f"Updated price for item {price} : ${prices[price]:.2f}" )
