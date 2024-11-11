# Consider seq = [5,9,12,4,7]
# Display the smallest number in our list

seq = [5,9,12,4,7]
small = seq[0]

for x in seq:
    if x < small:
        small = x

print("Smallest number in given list:",small)

