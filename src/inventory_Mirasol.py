# Function 1: 
def add_to_stock(stock_list):
    """Adds a fixed value to the inventory stock list"""
    stock_list.append(75)  
    print("Inside function (stock):", stock_list)  

# Test Function 1
inventory = [100, 200, 150]  
add_to_stock(inventory)  
print("Outside function (stock):", inventory)  

# Function 2: 
def update_price(price):
    """Calculates a 10% markup on the given price"""
    new_price = price + (price * 0.10)  
    print("Inside function (price):", new_price)  

# Test Function 2
base_price = 250.0 
update_price(base_price)  
print("Outside function (price):", base_price)  