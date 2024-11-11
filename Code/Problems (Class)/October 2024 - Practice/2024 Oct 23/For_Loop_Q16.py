# Question 7:

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if start > end:
    for i in range(start,end-1,-1):
        print(i,end="\t")
else:
    for i in range(start,end+1,1):
        print(i,end="\t")
