# Task 6: Consider a = [5,9,12,15,4] , Now find difference between biggest and smallest element without using list functions

a = [5,9,12,15,4]

big = a[0]
small = a[0]

for num in a:
    if num > big:
        big = num
    else:
        small = num

print("Biggest number:",big)
print("Smallest number:",small)

diff = big - small
print(f"difference between biggest element and smallest element is: {diff}")