# Task 6: Write a program to read filename, if file available display data otherwise display message as "Sorry! Your File is not Available"

try:
    fname = input("Enter File Name with Extension: ")
    file = open(fname,'r')
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("Sorry! Your File is not Available")
