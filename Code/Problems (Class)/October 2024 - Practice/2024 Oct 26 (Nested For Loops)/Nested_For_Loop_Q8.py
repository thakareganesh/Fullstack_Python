# Question 8: Print the following pattern
"""
A	B	C	D
A	B	C	D
A	B	C	D
A	B	C	D
"""

for row in range(1,5):
    alpha = 65
    for col in range(1,5):
        print(chr(alpha),end="\t")
        alpha = alpha + 1
    print()