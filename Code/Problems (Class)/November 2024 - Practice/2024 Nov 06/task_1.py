# Task 1: Write a program to check given number is prime or not


num = int(input('Enter any number: '))
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print(f"{i} is a prime number")
else:
    print(f"{i} is not a prime number")