# # Question 5: Print the following pattern
"""
*	*	*	*
$	$	$	$
*	*	*	*
$	$	$	$
*	*	*	*
"""

for row in range(1,6):
    for col in range(1,5):
        if row % 2 != 0:
            print("*",end="\t")
        else:
            print("$",end="\t")
    print()