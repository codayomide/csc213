# class exercise - user-auth

username = "codayomide"
password = "12345678"

username_entry = input("Input Username: ")
password_entry = input("Input Password: ")

if username_entry == username and password_entry == password:
  print('Access granted!')
else:
  print('Access denied!')