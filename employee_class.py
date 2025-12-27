class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}")
        employee1 = Employee(1, "Happy", "Master")
        print("employee name: =", employee1.name)
        print("Employee Department:= " , employee1.department)


class Manager(Employee):
    def __init__(self, emp_id, name, department, team_size):
        super().__init__(emp_id, name, department)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Role: Manager, Team Size: {self.team_size}")


class Developer(Employee):
    def __init__(self, emp_id, name, department, programming_language):
        super().__init__(emp_id, name, department)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Role: Developer, Language: {self.programming_language}")


class Intern(Employee):
    def __init__(self, emp_id, name, department, duration_months):
        super().__init__(emp_id, name, department)
        self.duration_months = duration_months

    def display_info(self):
        super().display_info()
        print(f"Role: Intern, Internship Duration: {self.duration_months} months")
