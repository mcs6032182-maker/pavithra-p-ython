import json

FILE = "trains.json"


# Load train data
def load_trains():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save train data
def save_trains(trains):
    with open(FILE, "w") as file:
        json.dump(trains, file, indent=4)


# Add a train
def add_train(trains):
    train = {
        "number": input("Enter Train Number: "),
        "name": input("Enter Train Name: "),
        "source": input("Enter Source: "),
        "destination": input("Enter Destination: "),
        "seats": int(input("Enter Available Seats: "))
    }

    trains.append(train)
    save_trains(trains)

    print("Train added successfully!")


# Search train
def search_train(trains):
    number = input("Enter Train Number: ")

    for train in trains:
        if train["number"] == number:
            print("\nTrain Found")
            print("Number      :", train["number"])
            print("Name        :", train["name"])
            print("Source      :", train["source"])
            print("Destination :", train["destination"])
            print("Seats       :", train["seats"])
            return

    print("Train not found!")


# Book a seat
def book_ticket(trains):
    number = input("Enter Train Number: ")

    for train in trains:
        if train["number"] == number:

            if train["seats"] > 0:
                train["seats"] -= 1
                save_trains(trains)
                print("Ticket booked successfully!")
                print("Remaining seats:", train["seats"])
            else:
                print("No seats available.")

            return

    print("Train not found!")


# Cancel a ticket
def cancel_ticket(trains):
    number = input("Enter Train Number: ")

    for train in trains:
        if train["number"] == number:
            train["seats"] += 1
            save_trains(trains)

            print("Ticket cancelled successfully!")
            print("Available seats:", train["seats"])
            return

    print("Train not found!")


# Delete a train
def delete_train(trains):
    number = input("Enter Train Number: ")

    for train in trains:
        if train["number"] == number:
            trains.remove(train)
            save_trains(trains)

            print("Train deleted successfully!")
            return

    print("Train not found!")


# Display all trains
def display_trains(trains):
    if len(trains) == 0:
        print("No trains available.")
        return

    print("\n========== TRAIN LIST ==========")

    for train in trains:
        print("Train Number :", train["number"])
        print("Train Name   :", train["name"])
        print("Source       :", train["source"])
        print("Destination  :", train["destination"])
        print("Seats        :", train["seats"])
        print("--------------------------------")


# Main program
trains = load_trains()

while True:

    print("\n===== TRAIN MANAGEMENT SYSTEM =====")
    print("1. Add Train")
    print("2. Search Train")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Delete Train")
    print("6. Display Trains")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_train(trains)

    elif choice == "2":
        search_train(trains)

    elif choice == "3":
        book_ticket(trains)

    elif choice == "4":
        cancel_ticket(trains)

    elif choice == "5":
        delete_train(trains)

    elif choice == "6":
        display_trains(trains)

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
