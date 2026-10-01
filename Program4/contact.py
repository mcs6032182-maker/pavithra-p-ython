import json

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def display_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for contact in contacts:
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("-------------------")


add_contact()
add_contact()
display_contacts()
