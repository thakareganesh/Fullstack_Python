# Question 5: read multiple items from customer (pid,cost) and then find bill amount.

dict1 = {}
billAmt = 0
ch = "y"
while ch == "y":
    pid = int(input("Enter product ID: "))
    pcost = eval(input("Enter product Cost: "))
    dict1[pid] = pcost
    ch = input("Do you want to continue(y/n): ")

print(f"My dictionary: {dict1}")

for key in dict1:
    billAmt = billAmt + dict1[key]

print(f"Final Bill is: {billAmt}")