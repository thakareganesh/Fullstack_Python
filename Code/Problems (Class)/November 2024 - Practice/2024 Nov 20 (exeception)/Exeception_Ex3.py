# Question 23: Exam

try:
    a = int(input("Enter any integer values: "))
    b = int(input("Enter any integer values: "))
    c = a//b
except ValueError:
    print("a,b values should be integers only")
except ZeroDivisionError:
    print("c values should not be zero")
print("Thank You")