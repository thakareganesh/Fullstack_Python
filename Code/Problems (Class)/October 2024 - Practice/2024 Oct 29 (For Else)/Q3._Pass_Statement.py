# Pass Statement Example

"""
age = int(input("Enter your age: "))
if age > 0:
    print("Valid Age")
    pass  # --> here we used pass statement as a placeholder for future code
else:
    print("Invalid Age")
"""
age = int(input("Enter your age: "))
if age > 0:
    print("Valid Age")
    if age >= 18:
        print("Eligible for vote")
    else:
        print("Not eligible for vote")
else:
    print("Invalid Age")