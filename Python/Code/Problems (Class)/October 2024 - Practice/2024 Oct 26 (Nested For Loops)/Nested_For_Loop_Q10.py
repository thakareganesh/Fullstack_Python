# Question 10: Print the following pattern
"""
*
*   *
*   *   *
*   *   *   *
*   *   *   *   *
"""
for row in range(1,6):
    for col in range(1,row+1):
        print("*",end="\t")
    print()