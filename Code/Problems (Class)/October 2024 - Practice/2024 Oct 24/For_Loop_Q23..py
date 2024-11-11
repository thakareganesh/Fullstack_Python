#Question 23: Consider seq = [5,9,12,15,7], Now print all numbers which are divisible by 5

seq = [5,9,12,15,7]
print("Following are the numbers in given list which are divisible by 5:")
for n in seq:
    if n % 5 == 0:
        print(n,end="\t")