
# Nested List Example 1: accessing values of nested list using by nested for loop
lst1 = [[10,20,30],[5,15,25],[35,40,45]]

# accessing nested list element in table-row format
for row in lst1:
    for col in row:
        print(col,end="\t")
    print()

print("=" * 30)

# accessing nested list element as it is
for row in lst1:
    print(row,end=" ")