# Q.1 : Read product ID, cost them create dictionary

dict1 = {}

pid = int(input("Enter Product ID: "))
pcost = eval(input("Enter Cost: "))

dict1[pid] = pcost
print(f"My Dict: {dict1}")