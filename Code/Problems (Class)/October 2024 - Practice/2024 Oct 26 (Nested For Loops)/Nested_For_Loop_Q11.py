# Question 11: Print the following pattern
"""
A
A   B
A   B   C
A   B   C   D
A   B   C   D   E
"""
for row in range(1,6):
    char = 65
    for col in range(1,row+1):
        print(chr(char),end="\t")
        char = char + 1
    print()