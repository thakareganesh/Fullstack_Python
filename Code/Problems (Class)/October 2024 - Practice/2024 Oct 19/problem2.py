"""
Problem 2: Write a program to read a number, if it is not a Zero, then only check given number is +ve number or -ve number
otherwise display message as Given number is Zero
"""

num = int(input("Enter any number: "))

if (num != 0):
    print("Given number is not Zero")
    if (num>0):
        print("Given number is +Ve Number")
    else:
        print("Given number is -Ve Number")

else:
    print("Given number is  Zero")
