password = input("Enter your password: ")

if len(password) >= 8 and not password.isalnum():
    print("Password is valid.")
else:
    print("Password is invalid.")

