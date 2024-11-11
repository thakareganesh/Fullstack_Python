# Task 9: read string contains number and  now find sum of all digits in given string

password = input("Enter your password: ")
sum = 0

for char in password:
    if char.isdigit():
        sum = sum + int(char)

print(f"Sum of all digits in password '{password}' is: {sum}")