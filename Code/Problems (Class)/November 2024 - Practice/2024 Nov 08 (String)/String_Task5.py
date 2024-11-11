# Task 1: Write a program to read a string then find number of digits

str1 = input("Enter any string: ")
c = 0
for i in str1:
    # if i>=str(0) and i<=str(9):  # --> its is also possible
    if i>='0' and i<='9':
        c = c + 1
print(f"In given string there are {c} number of digits.")