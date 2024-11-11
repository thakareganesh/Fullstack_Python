# Question 25: Consider seq = [5,9,12,15,7], Now read a number form user then check your number is available or not

seq = [5,9,12,15,7]
num = int(input("Enter any number: "))
yes = 0
# no = 0
for i in seq:
    if num == i:
        yes = i
    # else:
    #     no = i
if yes == num:
    print(f"{num} is Available in given list")
else:
    print(f"{num} is not Available in given list")