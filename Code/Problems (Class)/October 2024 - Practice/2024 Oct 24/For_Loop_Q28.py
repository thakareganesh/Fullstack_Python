# Question 28: Write a Program to check given number is perfect number or not --> 6,28,496,8128,

num = int(input("Enter any number: "))
div_sum = 0
for i in range(1,num):
    if num % i == 0:
        div_sum = div_sum + i
if div_sum == num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")

