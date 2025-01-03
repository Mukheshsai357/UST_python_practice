def view_items():
    print("Available Items:")
    for item, price in items.items():
        print(f"Name: {item}, Price: {price}")

def add_to_cart():
    item_name = input("Enter the item name: ")
    if item_name in items:
        quantity = int(input("Enter the quantity: "))
        for entry in cart:
            if entry[0] == item_name:
                entry[1] += quantity
                entry[3] = entry[1] * entry[2]
                print(f"{item_name} updated in the cart.")
                return
        cart.append([item_name, quantity, items[item_name], quantity * items[item_name]])
        print(f"{item_name} added to the cart.")
    else:
        print("Invalid item name. Please try again.")

def update_cart():
    item_name = input("Which item to update: ")
    for entry in cart:
        if entry[0] == item_name:
            quantity = int(input("Enter the new quantity: "))
            entry[1] = quantity
            entry[3] = entry[1] * entry[2]
            print(f"{item_name} updated in the cart.")
            return
    print(f"{item_name} is not in the cart.")

def delete_from_cart():
    item_name = input("Which item to remove: ")
    for entry in cart:
        if entry[0] == item_name:
            cart.remove(entry)
            print(f"{item_name} removed from the cart.")
            return
    print(f"{item_name} is not in the cart.")

def print_bill_1():
    print("Cart in List Format:")
    flat_cart = []
    for entry in cart:
        flat_cart.extend(entry)
    print(flat_cart)

def print_bill_2():
    print("Name, Quantity, Price, Total")
    total_amount = 0
    for entry in cart:
        print(f"{entry[0]}, {entry[1]}, {entry[2]}, {entry[3]}")
        total_amount += entry[3]
    print(f"Total Amount of Bill: {total_amount}")

while True:
    print("\nMenu:")
    print("Enter 1 for viewing the items")
    print("Enter 2 for adding item to cart")
    print("Enter 3 Update Items in Cart")
    print("Enter 4 Delete Items from Cart")
    print(" Enter 5 Print Cart as List")
    print("  Enter 6 Print Bill")
    print("7. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_items()
    elif choice == 2:
        add_to_cart()
    elif choice == 3:
        update_cart()
    elif choice == 4:
        delete_from_cart()
    elif choice == 5:
        print_bill_1()
    elif choice == 6:
        print_bill_2()
        break
    else:
        print("Invalid choice. Please try again.")
