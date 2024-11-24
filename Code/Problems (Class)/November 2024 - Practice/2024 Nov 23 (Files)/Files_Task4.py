# Task 4: Write a program to read filename then check total number of line in that file

fname = input("Enter File Name with Extension: ")
file = open(fname,'r')
data = file.readlines()
print(f"In \"{fname}\" file we have {len(data)} line of code")
file.close()