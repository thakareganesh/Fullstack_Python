# Consider seq = [5,9,12,4,7]
# Count no. of odd numbers

seq = [5,9,12,4,7,11]
count = 0

for i in seq:
    if i % 2 !=0:
        count = count + 1

print("No. of ODD counts:",count)