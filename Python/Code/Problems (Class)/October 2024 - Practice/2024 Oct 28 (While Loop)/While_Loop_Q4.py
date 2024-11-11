# Question 4: W.a.p to read multiple numbers from user until user say stop, then find sum of odd numbers in user list

ch = "y"
odd_sum = 0
while ch == "y":
    num = int(input("Enter any number: "))
    if num % 2 != 0:
        odd_sum = odd_sum + num
    ch = input("do you have any other number(y/n): ")
    # if ch == "n":
    #     break
print("Sum of Odd numbers from user list:", odd_sum)