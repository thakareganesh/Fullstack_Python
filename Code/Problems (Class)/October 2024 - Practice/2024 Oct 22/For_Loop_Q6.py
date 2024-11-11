# Consider seq = [5,9,12,4,7]
# Display the biggest number in our list

seq = [5,9,12,4,7]
big = seq[0]

for x in seq:
    if x > big:
        big = x

print("Biggest number in given list:",big)

