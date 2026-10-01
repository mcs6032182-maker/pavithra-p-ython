password = input("Enter password: ")

if len(password) >= 8 and any(c.isdigit() for c in password):
    print("Password is Strong")

    encrypted = ""
    for c in password:
        encrypted += chr(ord(c) + 3)

    file = open("password.txt", "w")
    file.write(encrypted)
    file.close()

    print("Encrypted password:", encrypted)
    print("Saved successfully.")
else:
    print("Password is Weak")