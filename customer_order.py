'''
exercise for the lap
'''

customer_name = input("What is the customer name ?")
customer_order_quintity=int(input(" What is order quantity ?"))
price_per_item=3.5

print(f"Dear: {customer_name}")
print(" Thank you for placing an order with us, please see the order details below")
print(f"Quintity Ordered := , {customer_order_quintity}")
print(f"Price Per Item :=  , {price_per_item}")
total_price=customer_order_quintity * price_per_item
print(f"Total Price Per Order := ",total_price)
print("===========================================")
print("Best Regards")
