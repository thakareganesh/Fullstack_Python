# Question 14: Print the following pattern
"""
                    *
                *       *
            *       *       *
        *       *       *       *
    *       *       *       *       *
"""

for row in range(1,6):
    for col in range(1,6-row):
        print(" ",end="\t")
    for col in range(1,row+1):
        print("\t*",end="\t")
    print()