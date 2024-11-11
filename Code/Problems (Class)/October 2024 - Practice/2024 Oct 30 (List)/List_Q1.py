# Question 1: Write a program to read numbers from user until they say stop , Then print all numbers

lst1 = []
ch = "y"
while ch == "y":
    num = int(input("Enter any number: "))
    lst1.append(num)
    ch = input("Do you want to continue(y/n): ")
print("Your elements are:",lst1)