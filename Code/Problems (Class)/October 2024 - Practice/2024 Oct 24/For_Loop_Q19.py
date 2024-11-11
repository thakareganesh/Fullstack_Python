# Question 19: Write a program to read number then find factorial of a given number

num = int(input("Enter any number: "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"factorial of {num} is: {fact}")