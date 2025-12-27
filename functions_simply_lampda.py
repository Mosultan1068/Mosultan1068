'''
this code snipit is to show how functions
are written and executed as part of the code
these are just simple functions.
some with parameters and some without, please see the example
'''

#using the input function as an input parameter
def add_users(pages=int(input("Please enter the number of pages to be printed: "))):
    price_per_page = 0.10

    # Lambda to calculate total price
    total_price=lambda p, price: pages * price

    #another method of doing the lambda function
    total_cost=(lambda price_per_page, pages:price_per_page * pages) (price_per_page, pages)
    print(f"Total price: £{total_price(pages, price_per_page):.2f}")

    # print(f"The price will be: {total_price(pages, price_per_page):.2f}")
    print(f"total cost will be £{total_cost :.2f}")



def show_calc():
#above is what is known as none-patramatized function

    price_item_1=int(input("Please enter the first item price: "))
    price_item_2=int(input("Please enter the second item price: "))
    total_price=float(price_item_1+price_item_1+price_item_2)
    print("The cost of the 2 items is", total_price)

# calling the functions
add_users()
show_calc()