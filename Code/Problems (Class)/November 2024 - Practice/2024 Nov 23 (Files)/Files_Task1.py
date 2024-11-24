# Task 1: Write a program to readline number from user then display the line

ln = int(input("Enter line of number: "))
file = open("Demo1.txt","r")
data = file.readlines()
print(f"{ln} line data is: {data[ln]}")
file.close()