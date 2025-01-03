items = ['Bread', 'Cookies', 'Butter', 'Cheese', 'Yoghurt']
values_of_items=[40,80,180,120,60]
cart = []  

while True:
    print("What do you want ?")
    print("Enter 1 for viewing the items")
    print("Enter 2 for adding item to cart")
    print("Enter 3 Update Items in Cart")
    print("Enter 4 Delete Items from Cart")
    print("Enter 5 Print Cart as List")
    print("Enter 6 Print Bill")
  
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Available Items:")
        for i in range(len(items)):
	        print("Name: "+items[i]+",price:"+values_of_items[i])   
    elif choice == 2:
        item_name = input("Enter the item name: ")
        if item_name in items:
            quantity = int(input("Enter the quantity: "))
            if(quantity<=0):
                print("invalid quantity")
            else:
                cart.append([item_name,quantity])
            
        else:
            print("Invalid item name. Please try again.")
    
    elif choice == 3:
        item_name = input("Which item to update: ")
        for item_and_quantity in cart:
            if(item_and_quantity[0]==item_name):
                quantity_update=int(input("enter the quantity to be updated:"))
                item_and_quantity[1]=quantity_update
        else:
            print(item_name+" is not in the cart.")
    
    elif choice == 4:
        item_name = input("Which item to remove: ")
        for item_and_quantity in cart:
            if(item_and_quantity[0]==item_name):
                del item_and_quantity
        else:
            print(item_name+" is not in the cart.")
    
    elif choice == 5:
        print("item name,  quantity,  value")
        for item_and_quantity in cart:
            temp=items.index(item_and_quantity[0])
            item_price=values_of_items[temp]*item_and_quantity[1]
            print(item_and_quantity[0],item_and_quantity[1],item_price)
         
    elif choice == 6:
        print("item_name, quantity, Price, Total")
        total = 0
        for item_and_quantity in cart:
            temp=items.index(item_and_quantity[0])
            item_price=values_of_items[temp]*item_and_quantity[1]
            total+=item_price
            print(item_and_quantity[0],item_and_quantity[1],values_of_items[temp],item_price)
        print("total_sum_of_items: "+total)
        break
    
    else:
        print("Invalid choice. Please try again.")
