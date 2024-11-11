"""
# Task 3: Write a program to read password from user, then check password is valid or invalid
Note: Password should be minimum 8 characters and maximum 14 characters at least 1 lowercase, 1 uppercase, 1 digit
and symbol required then its valid password otherwise it is invalid password
"""

password = input("Enter your password: ")
min_length = 8
max_length = 14
special_characters = "!@#$%^&*(),.?\":{}|<>"

has_lower = False
has_upper = False
has_digits = False
has_special = False

if len(password) >= min_length and len(password) <= max_length:
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digits = True
        elif char in special_characters:
            has_special = True
    if has_lower and has_upper and has_digits and has_special:
        print(f"{password} is a Valid Password")
    else:
        print("Invalid Password: There should be included at least 1 lowercase letter,1 uppercase letter, 1 digit and 1 special character.")
else:
    print("Invalid Password: Password length should be between 8 and 14 characters")
