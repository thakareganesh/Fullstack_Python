# Task 5: Write a program to read filename, line number from user then only display data

fname = input("Enter filename with extensions: ")
lineNo = int(input("Enter line number to display: "))

file = open(fname,'r')
data = file.readlines()

if lineNo <= len(data):
    print(data[lineNo])
else:
    print(f"Sorry! We have only {len(data)} lines in our \"{fname}\" File")
file.close()