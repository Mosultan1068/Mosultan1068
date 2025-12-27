'''
Store a product name,
base price,
and tax rate in variables, calculate the final price after
tax, and display all details in a formatted output.
'''
import time
#uk tax rate at 17.5%
v_product_tax_rate = 0.175

v_product_name = input("\tEnter the product name: ")
v_product_price = float(input("Enter the product price: "))

for character in v_product_name:
    time.sleep(1)
    print(character)
print(" ================================================ ")
print("The product name is: ",v_product_name)
print(f" The product price is: {v_product_price}")
print(f" the product tax rate is: {v_product_tax_rate} %")

print(" ---------------------------------------------- ")
v_final_price = (v_product_price * v_product_tax_rate) + v_product_price
print(f"The final price is: {v_final_price}")
print(" ------------------------------------------------")


