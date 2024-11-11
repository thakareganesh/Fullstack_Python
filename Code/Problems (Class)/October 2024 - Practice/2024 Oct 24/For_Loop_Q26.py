# Question 26: Consider seq = [5,9,12,5,7], Now read a number then check the occurrence of that number

seq = [5,9,12,5,7]
num = int(input("Enter any number: "))
yes = 0
count = 0
for i in seq:
    if num == i:
        yes = i
        count = count + 1
if yes == num:
    print(f"{num} is Available {count} times in given list")
else:
    print(f"{num} is not Available in given list")