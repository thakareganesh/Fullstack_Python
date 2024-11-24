# Question 24: Exam

try:
    a = int(input("Enter any integer value: "))
    b = int(input("Enter any integer value: "))
    try:
        c = a%b
    except ZeroDivisionError:
        print("c value should not be zero")
except ValueError:
    print("a,b values should be integers only")
print("Thank You")