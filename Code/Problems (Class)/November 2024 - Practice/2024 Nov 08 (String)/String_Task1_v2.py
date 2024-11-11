# Task 1: Write a program to read any string value then print only vowels

my_str = input("Enter any string: ")
# my_str = 'Sathya Technology'
print("Vowels are: ",end="")
vowels = 'aeiou'
for char in my_str:
    if char in vowels:
        print(char,end="\t")
