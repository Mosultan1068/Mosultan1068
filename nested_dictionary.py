
# Nested dictionary of electronic items
stocks_list = {
    "Electronics": {
        "Mobile": {"Price": 500, "Stock": 30, "Rating": 4.5},
        "Laptop": {"Price": 800, "Stock": 15, "Rating": 4.7}
    },
    "Clothing": {
        "Shirt": {"Price": 5, "Stock": 50, "Size": ["S", "M", "L"]},
        "Jeans": {"Price": 6, "Stock": 40, "Size": ["M", "L", "XL"]}
    },
    "Books": {
        "Novel": {"Price": 1, "Stock": 100, "Author": "John Smith"},
        "Textbook": {"Price": 2, "Stock": 20, "Author": "Dr. Brown"}
    }
}


for item, details in stocks_list.items():
    print(f"\n{item}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

print("Mobile_phone_price",stocks_list ["Electronics"]["Mobile"]["Price"])
#reducing the stock
stocks_list["Books"]["Novel"]["Stock"] -=30
#reducing the price
stocks_list["Electronics"]["Mobile"]["Price"] -=10
#adding a new item in the clothing section
stocks_list["Clothing"]["Top"] = {"Price": 10, "Stock": 30, "Size": ["M", "L", "XL"]}

for item, details in stocks_list.items():
    print(f"\n{item}:")
    for key, value in details.items():
        print(f"  {key}: {value}")