# Question 1: Write a program to read multiple numbers from user until they said stop. then find sum of all numbers.

sum = 0
ch = "y"
while ch == "y":
    num = int(input("Enter any number: "))
    sum = sum + num
    ch = input("Do you want to continue(y/n):")
print("Sum is:", sum)