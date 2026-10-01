password = input("Enter password: ")

if len(password) >= 8:
    print("Password is Valid")

    reversed_pass = password[::-1]
    encrypted = ""

    for c in reversed_pass:
        encrypted += chr(ord(c) + 2)

    with open("password.txt", "w") as file:
        file.write(encrypted)

    print("Encrypted data:", encrypted)
else:
    print("Password must contain at least 8 characters.")