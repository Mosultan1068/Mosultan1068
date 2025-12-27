# Parent class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def show_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}"

# Child classes inheriting from Employee
class DeliveryDriver(Employee):
    def __init__(self, name, employee_id, salary, truck_number):
        super().__init__(name, employee_id, salary)
        self.truck_number = truck_number

    def show_details(self):
        return super().show_details() + f", Truck: {self.truck_number}"

class WarehouseWorker(Employee):
    def __init__(self, name, employee_id, salary, shift):
        super().__init__(name, employee_id, salary)
        self.shift = shift

    def show_details(self):
        return super().show_details() + f", Shift: {self.shift}"

class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def show_details(self):
        return super().show_details() + f", Team Size: {self.team_size}"


driver1 = DeliveryDriver("John", 101, 40000, "Truck-12")
worker1 = WarehouseWorker("Alice", 202, 45000, "Night")
manager1 = Manager("Robert", 303, 90000, 10)

print(driver1.show_details())
print(worker1.show_details())
print(manager1.show_details())
