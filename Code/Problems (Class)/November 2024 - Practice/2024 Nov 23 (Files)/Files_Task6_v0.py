# Task 6: Write a program to read filename, if file available display data otherwise display message as "Sorry! Your File is not Available"

try:
    fname = input("Enter filename with extension: ")
    file = open(fname,'r')
except FileNotFoundError:
    print("Sorry..! Your file is not available.")
else:
    data = file.read()
    print(data)
    file.close()
