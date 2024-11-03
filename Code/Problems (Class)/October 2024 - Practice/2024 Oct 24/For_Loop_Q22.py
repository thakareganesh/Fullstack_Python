# Question 22: Write a program to read a number and find its prime number or not

num = int(input("Enter any number: "))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print(f"{num} is Prime Number")
else:
    print(f"{num} is not Prime Number")
