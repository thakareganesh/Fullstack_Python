# Question 1: Consider sequence as [4,9,12,8,5] now print only even numbers:

seq = [4,9,12,8,5]
print("Even numbers from given list:")
for x in seq:
    if x % 2 == 0:
        print(x,end="\t")