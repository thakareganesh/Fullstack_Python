# Question 27: Consider seq = [5,9,12,15,7] , Now print all numbers which are divisible by both 3 and 5
# Output : 15 --> in above list 15 is divided by both 3,5

seq = [5,9,12,15,7,30]
print("Following are the numbers which are divisible by both 3 and 5")
for i in seq:
    if (i % 3 == 0 and i % 5 == 0):
        print(i,end="\t")