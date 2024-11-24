# Question 21: Exam

try:
    a = int(input("Enter any integer value: "))
    b = int(input("Enter any integer value: "))
    c = a/b
except ValueError:
    print("a,b values should be integers only")