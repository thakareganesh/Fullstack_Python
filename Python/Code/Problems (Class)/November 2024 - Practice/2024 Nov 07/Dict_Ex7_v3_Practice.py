# Question 6: read multiple items from customer (pid,,pname,pcost) and then find bill amount.

mydict = {}
billAmt = 0
ch = "y"
while ch == "y":
    pid = int(input("Enter product Id: "))
    pname = input("Enter product Name: ")
    pcost = float(input("Enter product cost: "))
    mydict[pid] = [pname,pcost]
    ch = input("Do you want to continue(y/n): ")

print(f"My Dictionary: {mydict}")
for key in mydict.items():
    billAmt = billAmt + key[1][1]

print(f"Final Bill is: {billAmt}")
