'''
class ClassName:
    def __init__(self, value):
        self._attribute = value

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, new_value):
        if new_value < 1000:
            self._attribute = new_value
        else:
            raise ValueError("Value must be greater than 10000")

Value1=ClassName(1200)
print(Value1.attribute)

value1 = ClassName(990)
print(value1.attribute)

print("--------------------------------------------------------------------")
''' 
class Pilot:
    def __init__(self, salary):
        self._salary = salary  

    @property
    def salary(self):
        return self._salary  

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 100000:  
            self._salary = new_salary  
        else:
            raise ValueError("Salary must be at least $100,000")

#this is calling the getter method
pilot1 = Pilot(120000)
print(pilot1.salary)  

#this is calling the setter method
pilot1.salary = 130000 
print(pilot1.salary) 

#again this is calling to setter method to exhbit the error for the salary level
pilot1.salary = 90000
