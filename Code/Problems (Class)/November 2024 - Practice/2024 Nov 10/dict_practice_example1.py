# Dictionary practice example 1

dict1 = {101:"Ganesh",102:"Harshu",103:"Mukesh",104:"Akash",105:"Shubham"} 

# Displaying keys 
print("Your keys are:",end="\t")
for keys in dict1.keys():
    print(keys,end="\t")
print()

# Displaying values
print("Your values are:",end=" ")
for values in dict1.values():
    print(values,end="\t")
print()

# Displaying Key-Value pairs
print("Your Key-Values are:")
for key,values in dict1.items():
    print(key,'\t',values)

# Removing Record form current dictionary
eid = int(input("Enter EMP ID to remove record: "))
dict1.pop(eid)
print("Your employees are:",dict1)
