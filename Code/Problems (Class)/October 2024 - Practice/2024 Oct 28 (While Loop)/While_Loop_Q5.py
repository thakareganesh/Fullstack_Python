# Write a program to read multiple numbers until user say stop then find sum of even,odd numbers

ch = "y"
odd_sum = 0
even_sum = 0

while (ch == "y"):
    num = int(input("Enter any number: "))
    if (num % 2 == 0):
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num
    ch = input("Do you have any other number(y/n): ")
print("Sum of Odd Numbers:",odd_sum)
print("Sum of Even Numbers:",even_sum)
