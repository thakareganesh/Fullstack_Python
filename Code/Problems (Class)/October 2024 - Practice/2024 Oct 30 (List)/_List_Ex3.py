# 1. reverse()
# 2. sort()
# 3. count(element)
# 4. index(element)
from operator import indexOf, index

print("=" * 35)
# 4. index() is used to find index number of given element from list

lst4 = [105,9,15,5,9,12,5]
print("Your elements are:",lst4)
i = lst4.index(15)
print(f"15 is available in index no.: {i}")

j = lst4.index(5)
print(f"5 is available in index no.: {j}")