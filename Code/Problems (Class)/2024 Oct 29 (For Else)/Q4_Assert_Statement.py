# Assert statement example

age = int(input("Enter your age: "))
assert  (age > 0), "You've entered invalid age"
if (age >= 18):
    print("Eligible for vote")
else:
    print("Not eligible for vote")