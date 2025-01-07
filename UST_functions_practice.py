def total_trip_cost():
    kms=float(input("Enter the number of to drive :"))
    kms_per_ltr=float(input("Enter the number of kms per ltr(mileage) :"))
    cost_of_ltr=float(input("Enter the price of fuel per ltr :"))
    fuel_needed=kms/kms_per_ltr
    total_cost=fuel_needed*cost_of_ltr
    return total_cost
print(total_trip_cost())

def total_expenses():
    n=int(input("Enter the number of items to be purchased"))
    total_cost=0
    for i in range(n):
        quantity=int(input("Enter the quantity: "))
        price_of_item=float(input("ENter the price of item:"))
        if(quantity>10):
            cost=quantity*price_of_item
            total_cost+=(90*cost)/100
        else:
            total_cost+=quantity*price_of_item
    return total_cost
print(total_expenses())
