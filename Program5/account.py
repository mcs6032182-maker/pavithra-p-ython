class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def withdraw(self, amount):
        print("Savings Account")
        super().withdraw(amount)


class CurrentAccount(Account):
    def withdraw(self, amount):
        print("Current Account")
        super().withdraw(amount)


a1 = SavingsAccount("Rahul", 10000)
a2 = CurrentAccount("Priya", 15000)

a1.deposit(2000)
a1.withdraw(3000)
a1.show()

print()

a2.deposit(5000)
a2.withdraw(4000)
a2.show()
