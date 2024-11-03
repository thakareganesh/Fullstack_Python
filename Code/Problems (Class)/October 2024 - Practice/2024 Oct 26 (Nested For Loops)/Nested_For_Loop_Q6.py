# Question 6: Print the following pattern
"""
*	*	*	*
$	$	$	$
*	*	*	*
$	$	$	$
@	@	@	@
"""

for row in range(1,6):
    for col in range(1,5):
        if row == 1 or row == 3:
            print("*",end="\t")
        elif row == 2 or row == 4:
            print("$",end="\t")
        else:
            print("@",end="\t")
    print()