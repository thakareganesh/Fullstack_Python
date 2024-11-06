# Dictionary Example

order = {}
ch = "y"
while ch == "y":
    pid = int(input("Enter product id: "))
    pname = input("Enter product name: ")
    cost = float(input("Enter product cost: "))
    order[pid]= [pname,cost]
    ch = input("Do you want to continue(y/n): ")

print("pid","\t  pname","\t  cost")
for pid,pname in order.items():
    print(pid,end="\t\t")
    sum = 0
    for j in pname:
        print(j,end="\t\t")
    for j, k in order.values():
        sum = sum + k
    print()

print("=" * 27)
print(f"final bill is: {sum}")
print("=" * 27)


