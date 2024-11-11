# Question 1: Write a program to check given hall ticket number is passed or not in list

passed_ht = [1122,1564,1356,1175,1248]
ht = int(input("Enter your hallticket number: "))
for std in passed_ht:
    if std == ht:
        print("Pass")
        break
else:
    print("Fail")