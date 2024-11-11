"""
Question: Write a program to read subject marks from user, in-case user enter a value less than 0 or greater than 100 then
only display message as Invalid Marks Otherwise don't display message.
"""

marks = int(input("Enter your marks: "))
if (marks<0 or marks>100):
    print("Invalid marks")