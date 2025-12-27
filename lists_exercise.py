'''
exercise to play with lists
'''

purchase_history=[
    ["Laptop", 1200.00],
    ["Headphones", 150.00],
    ["Backpack", 75.50],
    ["Smartphone", 300.99],
    ["Water Bottle", 20.00],
    ["usb drive", 30.00]
]

for i in purchase_history:
    print(i)

def show_purchases(history, n=5):
    recent_purchases=history [-n:]
    print("\n Recent Purchases List", recent_purchases)


show_purchases(purchase_history)