
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):  # getter for name
        return self._name

    @name.setter
    def name(self, new_name):  # setter for name
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def salary(self):  # getter for salary
        return self._salary

    @salary.setter
    def salary(self, new_salary):  # setter for salary
        if isinstance(new_salary, (int, float)) and new_salary > 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary must be a positive number")

# Usage:
emp = Employee("Alice", 1000)
print(emp.name, emp.salary)   # calls getters
emp.name = "Bob"              # calls name setter
emp.salary = 2000             # calls salary setter
print(emp.name, emp.salary)
