grocery_inventory = {
    "Milk" : ("Dairy", 3.50, 8),
    "Eggs" : ("Dairy", 5.50, 30),
    "Bread" : ("Bakery", 2.99, 15),
    "Apples" : ("Produce", 1.50, 50),
}
eggs_price = grocery_inventory["Eggs"][1]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    eggs_price_reduced = eggs_price - 1
    category, _ , stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, eggs_price_reduced, stock)
else:
    print("The price of Eggs is reasonable")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
if grocery_inventory["Milk"][2] < 10:
    category, price, stock = grocery_inventory["Milk"]
    stock_updated = stock + 20
    grocery_inventory["Milk"] = (category, price, stock_updated)
    print("milk needs to be restocked. increasing stock by 20 units.")
else:
    print("Milk has sufficient stock")
if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:", grocery_inventory)
    
