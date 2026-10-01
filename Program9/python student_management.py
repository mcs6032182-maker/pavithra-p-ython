# Student Record Management System
# Single Python File

students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "phone": phone
    }

    students.append(student)

    print("\nStudent added successfully!")


def view_students():
    print("\n--- Student List ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-" * 40)
        print("ID     :", student["id"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("Course :", student["course"])
        print("Email  :", student["email"])
        print("Phone  :", student["phone"])


def view_student():
    print("\n--- Student Details ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print("-" * 40)
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            print("Email  :", student["email"])
            print("Phone  :", student["phone"])
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            print("Leave blank to keep the old value.")

            name = input(f"Name [{student['name']}]: ")
            age = input(f"Age [{student['age']}]: ")
            course = input(f"Course [{student['course']}]: ")
            email = input(f"Email [{student['email']}]: ")
            phone = input(f"Phone [{student['phone']}]: ")

            if name:
                student["name"] = name

            if age:
                student["age"] = age

            if course:
                student["course"] = course

            if email:
                student["email"] = email

            if phone:
                student["phone"] = phone

            print("\nStudent updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            print("\nStudent deleted successfully!")
            return

    print("Student not found.")


def main():

    while True:

        print("\n")
        print("=" * 45)
        print("      STUDENT RECORD MANAGEMENT")
        print("=" * 45)

        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Details")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            view_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("\nThank you!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
1