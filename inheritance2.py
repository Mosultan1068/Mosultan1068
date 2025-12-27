class Vehicle:
    def info(self):
        return "This is a vehicle from the parent class"

class Car(Vehicle):
    def type(self):
        return "This is a car from the car class"

class Engine:
    def engine_info(self):
        return "This car has an engine"
class Electric:
    def battery_info(self):
        return "This car runs on a battery"

class ElectricCar(Engine, Electric):
    pass
'''

class Animal:
    def species(self):
        return "This is an animal"

class Mammal(Animal):
    def mammal_info(self):
        return "This is a mammal"

class Dog(Mammal):
    def sound(self):
        return "Dogs bark"

class Phone:
    def brand(self):
        return "This is a phone"

class Smartphone(Phone):
    def type(self):
        return "This is a smartphone"

class Landline(Phone):
    def type(self):
        return "This is a landline phone"

class Employee:
    def details(self):
        return "This is an employee"

class Manager(Employee):
    def role(self):
        return "Manages the team"

class Engineer(Employee):
    def role(self):
        return "Develops the product"

class TechLead(Manager, Engineer):
    def lead_info(self):
        return "Leads both management and engineering"
'''

car = Car()
print(car.info())
print(car.type())

electric_car = ElectricCar()
print(electric_car.engine_info())
print(electric_car.battery_info())

'''

dog = Dog()
print(dog.species())
print(dog.mammal_info())
print(dog.sound())

smartphone = Smartphone()
landline = Landline()
print(smartphone.brand())
print(smartphone.type())
print(landline.type())

tech_lead = TechLead()
print(tech_lead.details())
print(tech_lead.role())
print(tech_lead.lead_info())
'''