
# Define a class
class Bike:
    def __init__(self, name, gear):
        # this is an example of a paramatarized constructor
        # it takes self + name and gear for the class
        self.name = name            # instance attribute
        self.gear = gear            # instance attribute
        print(f"New Bike has been created {self.name} , {self.gear} created")
        print("--------------------------------------")

    def __del__(self):
        #delete an existing bike
        print(f" Existing bike has been deleted : {self.name}, {self.gear} has been deleted")

    def display(self):
        #logic to display the bike
        if self.gear == 12:
            print(f"12-Bike Name: {self.name}, Gears: {self.gear}")
        else:
            print(f"others-Bike Name: {self.name}, Gears: {self.gear}")

# Create an object of the class
bike1 = Bike("Mountain Bike", 11)
bike2 = Bike("Mountain Bike", 12)

# Call the method
bike1.display()
bike2.display()
del bike2