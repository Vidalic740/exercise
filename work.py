username = "you"
password = "me"

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

if input_username == username and input_password == password:
    print("Login successful")
else:
    print("Invalid credentials")