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

pilot1 = Pilot(120000)
print(pilot1.salary)

pilot1.salary = 130000
print(pilot1.salary)

pilot1.salary = 100000
print(pilot1.salary)