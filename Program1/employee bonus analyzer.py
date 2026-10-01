name = input("Enter employee name: ")
salary = float(input("Enter salary: "))
experience = int(input("Enter experience in years: "))

if experience >= 10:
    bonus = salary * 0.20
elif experience >= 5:
    bonus = salary * 0.15
elif experience >= 2:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

total_salary = salary + bonus

print("\nEmployee:", name)
print("Salary:", salary)
print("Bonus:", bonus)
print("Total Salary:", total_salary)