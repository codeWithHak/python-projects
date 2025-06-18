print(f"{"-"*20} Mamu Shop {"-"*20}")

items = [
    {"name": "Rice", "price": 50, "quantity": 10},
    {"name": "Wheat Flour", "price": 40, "quantity": 8},
    {"name": "Sugar", "price": 45, "quantity": 6},
    {"name": "Salt", "price": 20, "quantity": 15},
    {"name": "Oil", "price": 120, "quantity": 5},
    {"name": "Daal", "price": 70, "quantity": 7},
    {"name": "Tea", "price": 150, "quantity": 3},
    {"name": "Milk", "price": 60, "quantity": 12},
    {"name": "Eggs", "price": 6, "quantity": 30},
    {"name": "Ketchup", "price": 90, "quantity": 4}
]

user_input = input("Item name: ")
user_cart = {'items':[], 'total':0}
for item in items:
    if item["name"].lower() == user_input.lower():
        
        print(f"Shopkeeper: {item['name']} available!\n")
        print(f"Customer: Ok, for how much?\n")
        print(f"Shopkeeper: For just {item["price"]}")
        
        user_input = int(input("How much do you want? "))
        
        if user_input <= item['quantity']:
            user_cart['items'] = {
                'name':item['name'],
                'price':item['price'],
                'quantity':user_input,
                }
            user_cart['total'] = item['price'] * user_input
            items['quantity'] -= user_input
            print("\nHere you go!")
            print(f"Your bill is: {user_cart}")
        else:
            print(f"Not eonugh stock! \n Only {item['quantity']} available")
            
        
        break
    else:
        print("not found!")

