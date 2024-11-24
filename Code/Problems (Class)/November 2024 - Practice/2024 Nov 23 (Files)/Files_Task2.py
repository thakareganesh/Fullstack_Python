# Task 2: Write a program to display total number of lines in our file

file = open("Demo1.txt",'r')
data = file.readlines()
print(f"There are {len(data)} lines in our file")
file.close()