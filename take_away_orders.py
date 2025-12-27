# Restaurant Menu Selector

# Step 1: Welcome message
print("Welcome to the Restaurant Menu Selector!")

# Step 2: Display menu items
print("\nToday's Menu:")
print("1. Pizza - $12")
print("2. Burger - $8")
print("3. Pasta - $10")
print("4. Salad - $7")

# Step 3: Get the user's menu choice as input
choice = int(input("\nEnter the number of the item you want to order: "))

quantity = int(input("Enter the quantity: "))

# Step 4: Initialize item name and price variables
item = ""
price = 0

# Step 5: Determine the item and price based on the user's choice (without nested if statements)
if choice == 1:
    item = "Pizza"
    price = 12
elif choice == 2:
    item = "Burger"
    price = 8
elif choice == 3:
    item = "Pasta"
    price = 10
elif choice == 4:
    item = "Salad"
    price = 7
else:
    item = "Invalid"
    price = 0

# Step 6: Calculate the total price by multiplying the price by the quantity
total_price = price * quantity

# Step 7: Check if the item is valid and display the order summary
if item != "Invalid":
    print("\nOrder Summary:")
    print("Item:", item)
    print("Quantity:", quantity)
    print("Total Bill: $", total_price)
else:
    print("\nInvalid choice! Please select a valid item from the menu.")
