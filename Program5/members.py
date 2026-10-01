class Book:
    def __init__(self, title):
        self.title = title
        self.issued_to = None

    def show(self):
        if self.issued_to:
            print(self.title, "- Issued to", self.issued_to)
        else:
            print(self.title, "- Available")


class User:
    def __init__(self, name):
        self.name = name

    def membership(self):
        return "Normal Member"

    def issue_book(self, book):
        if book.issued_to is None:
            book.issued_to = self.name
            print(self.name, "issued", book.title)
        else:
            print("Book is already issued.")

    def return_book(self, book):
        if book.issued_to == self.name:
            book.issued_to = None
            print(self.name, "returned", book.title)
        else:
            print("This book was not issued to", self.name)


class Student(User):
    def membership(self):
        return "Student Member"


class Faculty(User):
    def membership(self):
        return "Faculty Member"


class PremiumUser(User):
    def membership(self):
        return "Premium Member"


# Create books
book1 = Book("Python Programming")
book2 = Book("Artificial Intelligence")

# Create users
users = [
    Student("Rahul"),
    Faculty("Priya"),
    PremiumUser("Arun")
]

# Polymorphism
for user in users:
    print("\nName:", user.name)
    print("Membership:", user.membership())

# Issue books
users[0].issue_book(book1)
users[1].issue_book(book2)

print("\nBook Status:")
book1.show()
book2.show()

# Return book
print()
users[0].return_book(book1)

print("\nFinal Book Status:")
book1.show()
book2.show()