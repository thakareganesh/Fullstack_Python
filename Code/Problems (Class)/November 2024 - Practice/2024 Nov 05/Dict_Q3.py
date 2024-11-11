# Question 3: Read Employee Name and then remove record.

dict1 = {101:"Ganesh", 102:"Shubham",103:"Dhamma",104:"Karan",105:"Ashok"}

empName = input("Enter Employee Name: ")
found = False

for eid,name in dict1.items():
    if empName == name:
        dict1.pop(eid)
        print(f"{empName} is removed from the record")
        break
else:
    print(f"{empName} is not found in the records")

print(f"Current Records are: {dict1}")
