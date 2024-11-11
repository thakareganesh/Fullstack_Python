# Question 20: Write a program to read a number and print all divisible of that number.

num = int(input("Enter any number: "))
for i in range(1,num+1):
    if ( num % i == 0 ):
        print(i,end="\t")