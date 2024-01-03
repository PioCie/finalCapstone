# Create a list called menu, which items sold in cafe.
menu = ["Expresso", "Americano", "Late", "Cappuccino", "Babyccino"]
# Create a dictionary with the stock value for each item on menu.
stock = {"Expresso": 120,
         "Americano": 80,
         "Late": 60,
         "Cappuccino": 40,
         "Babyccino": 30}
# Create a dictionary with the prices for each item on menu.
price = {"Expresso": 2.10,
         "Americano": 2.35,
         "Late": 2.79,
         "Cappuccino": 2.69,
         "Babyccino": 0.99}
# Creating an empty variable for storage total stock value.
total_stock = 0
# I create a for loop to iterate over items on the menu list.
for item in menu:
    # Using menu items as a key to dictionaries with number of stocks and prices to calculate the value of each item
    # in each iteration.
    item_value = stock[item] * price[item]
    # Adding the value of an item to the total stock in each iteration.
    total_stock += item_value
# Printing out the total_stock result.
print(f"The total stock value in your coffee shop is {total_stock:.2f} £.")
