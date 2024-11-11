# Question 6:

num = int(input("Enter any number: "))
print("ODD","\tEVEN")
for i in range(1,num+1):
    if i % 2 != 0:
        print(i,end="\t\t")
    else:
        print(i)