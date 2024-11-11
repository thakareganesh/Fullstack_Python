"""
Problem 1: Write a program to read age of a person if it is +ve number then only check person is eligible
for vote or not, Otherwise display message as Invalid Age.
"""

age = int(input("Enter your age: "))
if (age>0):
    print("Valid Age")
    if (age>=18):
        print("Eligible for Vote")
    else:
        print("Not Eligible for Vote")

else:
    print("Invalid Age")