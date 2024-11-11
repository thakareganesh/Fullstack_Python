# Question 29: Write a program to read a number then check given number is prime or not
# if given number is prime number then only print that number

num = int(input("Enter any number: "))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print(num)