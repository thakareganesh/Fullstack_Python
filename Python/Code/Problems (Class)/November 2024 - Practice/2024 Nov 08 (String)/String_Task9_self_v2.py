# Task 4: Consider string is 'Sat3h5y1a' now find sum of all digits

str1 = "Sat3h5y1a"
sum = 0
for char in str1:
    # if char.isdigit():
    if char >= "0" and char <= "9":
        sum = sum + int(char)
print(f"Sum of all digits in string '{str1}' is: {sum}")
