# Question 4: Read multiple products (id,name and cost) and then store into dictionary

dict1 = {}
ch = "y"
while ch == "y":
    pid = int(input("Enter product ID: "))
    pname = input("Enter product Name: ")
    pcost = eval(input("Enter product Cost: "))
    dict1[pid] = [pname,pcost]
    ch = input("Do you want to continue(y/n): ")
print(f"My Dictionary: {dict1}")