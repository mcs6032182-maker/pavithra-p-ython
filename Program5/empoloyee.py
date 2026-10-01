class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 10000


class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 5000


class Intern(Employee):
    def calculate_salary(self):
        return self.salary + 2000


employees = [
    Manager("Arun", 40000),
    Developer("Kumar", 30000),
    Intern("Anu", 15000)
]

for employee in employees:
    employee.display()
    print("----------------")
