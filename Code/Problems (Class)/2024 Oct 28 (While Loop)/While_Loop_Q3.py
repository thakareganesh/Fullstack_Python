# Question 3: W.a.p to read multiple numbers from user until user say stop, then find sum of even numbers in user list

ch = "y"
even_sum = 0
while ch == "y":
    num = int(input("Enter any number: "))
    if num % 2 == 0:
        even_sum = even_sum + num
    ch = input("do you have any other number(y/n): ")
    # if ch == "n":
    #     break
print("Sum of even numbers from user list:",even_sum)