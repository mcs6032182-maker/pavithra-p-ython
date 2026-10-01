class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", self.author, "-", status)


class User:
    def __init__(self, name):
        self.name = name

    def issue_book(self, book):
        if book.available:
            book.available = False
            print(self.name, "issued", book.title)
        else:
            print("Book is already issued.")

    def return_book(self, book):
        if not book.available:
            book.available = True
            print(self.name, "returned", book.title)
        else:
            print("Book is already available.")


class Student(User):
    def issue_book(self, book):
        print("Student:", self.name)
        super().issue_book(book)


class Teacher(User):
    def issue_book(self, book):
        print("Teacher:", self.name)
        super().issue_book(book)


# Create objects
book1 = Book("Python Programming", "James")
book2 = Book("Web Development", "John")

student = Student("Rahul")
teacher = Teacher("Priya")

# Display books
book1.display()
book2.display()

print()

# Issue books
student.issue_book(book1)
teacher.issue_book(book2)

print()

# Return books
student.return_book(book1)
teacher.return_book(book2)

print()

# Display again
book1.display()
book2.display()
