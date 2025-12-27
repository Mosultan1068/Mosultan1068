'''
to demonstrate the use of tenary operator
'''

num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))

number_of_guests = int(20)
#below line demonstrates the tenary operator
print("Great") if num1 > num2 else print("Not Great")

hall="large Hall" if number_of_guests >= 20 else "small Hall"
print(hall)

