# Task 1: Write a program to read a string then find number of lowercase letters.

mystr = input("Enter any string: ")
count = 0
for char in mystr:
    if char >= "a" and char <= "z":
        count = count + 1

print("Number of lowercase letters:",count)