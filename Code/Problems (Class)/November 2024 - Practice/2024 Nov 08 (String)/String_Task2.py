# Task 2: Write a program to read any string then print only vowels without duplicates

my_str = input("Enter any string: ")
# my_str = "Sathya Technology"
vowels = 'aeiou'
no_duplicate = set()
for char in my_str:
    if char in vowels:
        no_duplicate.add(char)

# print(no_duplicate)
for char in no_duplicate:
    print(char,end="\t")