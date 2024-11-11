# Task 2: Write a program to read a string and then find no. of lowercase, uppercase, digits and symbols

str1 = input("Enter any string: ")
lower_count = 0
upper_count = 0
digits_count = 0
symbols_count = 0

for i in str1:
    if i >= "a" and i<="z":
        lower_count += 1
    elif i >= "A" and i<="Z":
        upper_count += 1
    elif i >= "0" and i <= "9":
        digits_count += 1
    else:
        symbols_count += 1


print(f"Number of Lower Case Count: {lower_count}")
print(f"Number of Upper Case Count: {upper_count}")
print(f"Number of Digits Count: {digits_count}")
print(f"Number of Symbols Count: {symbols_count}")
