# Question 2: print following pattern
"""
0	1	2	3
-1	0	1	2
-2	-1	0	1
"""

for row in range(1,4):
    for col in range(1,5):
        print(col-row,end="\t")
    print()