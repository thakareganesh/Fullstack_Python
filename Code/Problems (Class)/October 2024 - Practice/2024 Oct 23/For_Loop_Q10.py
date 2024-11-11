

num = int(input("Enter any number: "))
sum = 0
for i in range(1,num+1):
    print(i,end="\t")
    sum = sum + i
print("\nSum is:",sum)