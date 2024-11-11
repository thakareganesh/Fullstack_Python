# Question 24: Consider seq = [5,9,12,15,7], Now find difference between the biggest number and smallest number

seq = [5,9,12,15,7]
big = seq[0]
small = seq[0]
for i in seq:
    if i > big:
        big = i
    elif i < small:
        small = i
print("Biggest number:",big)
print("Smallest number:",small)

diff = big - small
print(f"Difference between {big} and {small} is: {diff}")