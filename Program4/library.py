import json

FILE = "library.json"


# Load books from file
def load_books():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save books to file
def save_books(books):
    with open(FILE, "w") as file:
        json.dump(books, file, indent=4)


# Add a book
def add_book(books):
    book = {
        "id": input("Enter Book ID: "),
        "title": input("Enter Book Title: "),
        "author": input("Enter Author Name: "),
        "status": "Available"
    }

    books.append(book)
    save_books(books)

    print("Book added successfully!")


# Search a book
def search_book(books):
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found")
            print("ID     :", book["id"])
            print("Title  :", book["title"])
            print("Author :", book["author"])
            print("Status :", book["status"])
            return

    print("Book not found!")


# Issue a book
def issue_book(books):
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Available":
                book["status"] = "Issued"
                save_books(books)
                print("Book issued successfully!")
            else:
                print("Book is already issued.")

            return

    print("Book not found!")


# Return a book
def return_book(books):
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                book["status"] = "Available"
                save_books(books)
                print("Book returned successfully!")
            else:
                print("Book is already available.")

            return

    print("Book not found!")


# Delete a book
def delete_book(books):
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)
            print("Book deleted successfully!")
            return

    print("Book not found!")


# Display all books
def display_books(books):
    if len(books) == 0:
        print("No books available.")
        return

    print("\n----- Library Books -----")

    for book in books:
        print("ID     :", book["id"])
        print("Title  :", book["title"])
        print("Author :", book["author"])
        print("Status :", book["status"])
        print("------------------------")


# Main program
books = load_books()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Display Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book(books)

    elif choice == "2":
        search_book(books)

    elif choice == "3":
        issue_book(books)

    elif choice == "4":
        return_book(books)

    elif choice == "5":
        delete_book(books)

    elif choice == "6":
        display_books(books)

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")