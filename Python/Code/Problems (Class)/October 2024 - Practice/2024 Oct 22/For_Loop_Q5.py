# Consider seq = [5,9,12,4,7]
# Find sum of even and odd numbers

seq = [5,9,12,4,7]
odd_sum = 0
even_sum = 0

for i in seq:
    if (i % 2 == 0):
        even_sum = even_sum + i
    if (i % 2 != 0):
        odd_sum = odd_sum + i
print("Sum of Even Numbers:",even_sum)
print("Sum of Odd Numbers:",odd_sum)