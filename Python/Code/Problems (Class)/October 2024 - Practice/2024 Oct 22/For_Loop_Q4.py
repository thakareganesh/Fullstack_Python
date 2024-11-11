# Consider seq = [5,9,12,4,7]
# Display all numbers divisible by 3

seq = [5,9,12,4,7]
print("All numbers in given sequence that is divisible by 3:")
for i in seq:
    if (i % 3 == 0):
        print(i)