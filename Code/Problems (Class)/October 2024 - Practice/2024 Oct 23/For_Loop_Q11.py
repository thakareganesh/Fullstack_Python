#

num = int(input("Enter any number: "))
product = 1
for i in range (1,num+1):
    print(i,end="\t")
    product = i * product
print("\nProduct is:",product)