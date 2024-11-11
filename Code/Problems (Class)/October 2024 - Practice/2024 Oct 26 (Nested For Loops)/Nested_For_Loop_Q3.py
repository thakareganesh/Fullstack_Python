# Question 3: Print following pattern
"""
1	2	3	4
5	6	7	8
9	10	11	12
"""


k = 0
for row in range(1,4):
    for col in range(1,5):
        k = k + 1
        print(k,end="\t")
    print()
        