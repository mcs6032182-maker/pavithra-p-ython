password = input("Enter password: ")

if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
    print("Strong Password")

    key = 5
    encrypted = ""

    for c in password:
        encrypted += chr(ord(c) ^ key)

    with open("password.txt", "w") as file:
        file.write(encrypted)

    print("Encrypted password saved.")
else:
    print("Weak Password")