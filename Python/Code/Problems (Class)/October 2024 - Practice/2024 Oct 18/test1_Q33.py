"""
Questin 33: Write a program  to read age in-case age is between 18 and 25 then display you are eligible to apply for job
otherwise display message as Sorry invalid age.
"""
age = int(input("Enter your age: "))
if (age>=18 and age<=25):
    print("You are eligible to apply for this Job")
else:
    print("Sorry, Invalid Age")