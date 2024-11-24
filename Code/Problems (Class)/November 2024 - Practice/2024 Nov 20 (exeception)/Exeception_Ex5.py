# Question 25: Exam

try:
    a = int(input("Enter any integer value: "))
    b = int(input("Enter any integer value: "))
    try:
        c = a % b
        d = int(input("Enter any number: "))
        try:
            e = d/c
        except ValueError:
            print("d value should be integers only")
    except ZeroDivisionError:
        print("c value should not be zero")
except ValueError:
    print("a,b values should be integers only")

print("Thank You")