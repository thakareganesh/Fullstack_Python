# Question 22: Exam

a = int(input("Enter any integer values: "))
b = int(input("Enter any integer values: "))
try:
    c = a/b
except ZeroDivisionError:
    print("C value should not be zero")
print("Thank You")