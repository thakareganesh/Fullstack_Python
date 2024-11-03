# Question 30: Write a program to read 1 to 100 prime numbers

for num in range(1,100):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num,end="\t")