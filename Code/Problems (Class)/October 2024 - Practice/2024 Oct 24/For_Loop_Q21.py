# Question 21: Write a program to read n value then count of that no. of divisible for that number

num = int(input("Enter any number: "))
count = 0
for i in range(1,num + 1):
    if (num%i==0):
        print(i,end="\t")
        count = count + 1
print(f"\nCount of {num} is: {count}")
