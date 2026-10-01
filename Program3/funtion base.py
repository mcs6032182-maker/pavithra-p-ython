def validate(password):
    return (len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password))

def encrypt(password):
    result = ""
    for c in password:
        result += chr(ord(c) + 4)
    return result

password = input("Enter password: ")

if validate(password):
    encrypted = encrypt(password)

    with open("secure.txt", "w") as file:
        file.write(encrypted)

    print("Password is Strong")
    print("Encrypted data:", encrypted)
    print("Data stored in secure.txt")
else:
    print("Password is Weak")