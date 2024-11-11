
# Question: Write a condition to check given character is alphabet or not

char = input("Enter any character: ")
if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")