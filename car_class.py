'''
this is my first class created in python
this class uses a car as a blue print
'''

class car:
    brand="ford"
    color="red"
    price=31000


    def details(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Price: {self.price}")

car1=car()
car1.details()
print()

#this enables the change of the attributes by adding a new car
car1.brand="Volks"
car1.color="White"
car1.price=22000

car1.details()