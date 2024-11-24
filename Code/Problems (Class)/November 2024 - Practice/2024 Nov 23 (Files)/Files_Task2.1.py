# Task 2: Write a program to display total number of lines in our file
fname = input("Enter file name with extension: ")
file = open(fname,'r')
data = file.readlines()
print(f"There are {len(data)} lines in our \"{fname}\" file")
file.close()