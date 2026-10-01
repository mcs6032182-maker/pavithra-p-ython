import matplotlib.pyplot as plt

months = []
expenses = []

n = int(input("Enter number of months: "))

for i in range(n):
    month = input("Enter month: ")
    expense = float(input("Enter expense: "))

    months.append(month)
    expenses.append(expense)

plt.figure(figsize=(15, 5))

# Line Chart
plt.subplot(1, 3, 1)
plt.plot(months, expenses, marker="o", color="blue")
plt.title("Monthly Expense Trend")
plt.xlabel("Month")
plt.ylabel("Expense")
plt.xticks(rotation=45)
plt.grid(True)

# Bar Chart
plt.subplot(1, 3, 2)
plt.bar(months, expenses, color="orange")
plt.title("Monthly Expense Comparison")
plt.xlabel("Month")
plt.ylabel("Expense")
plt.xticks(rotation=45)

# Pie Chart
plt.subplot(1, 3, 3)
plt.pie(
    expenses,
    labels=months,
    autopct="%1.1f%%"
)
plt.title("Expense Distribution")

plt.suptitle("Monthly Expense Dashboard", fontsize=16)
plt.tight_layout()
plt.show()