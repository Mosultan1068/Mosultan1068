class test:
    def __init__(self, val1, val2,val3):
        self.val1 = val1
        self.val2 = val2
        self.__val3 = val3
        print("Beggining of the constructor, the 3 values have been set")

    def __str__(self):
        return f"Test object with val1={self.val1}, val2={self.val2} , val3={self.__val3}"

    def show_basic_info(self):
        print(f"this is the value of val 1 and 2: {val1}, {val2}")
        print("this is show basic info")

    def process_values(self):
        print(val1, val2,val3)
        print("This is the process values defination")

    def __del__(self):
        print("end of __del__ deconstructor")

#setting the values for the constructor
val1 = 300
val2 = 400
val3 = 500
myvalues = test(val1, val2, val3)
print(myvalues)

#passing the values to the next defination for processing
myvalues.process_values()

#calling the show basic
# val 3 is hiddent because we are using __ in the constructor
myvalues.show_basic_info()
#print(myvalues.val3)

#deleting the values from the deconstructor
del myvalues
