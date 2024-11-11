# Question 1: Read EmpID then remove that record

dict1 = {101: "Ganesh", 102: "Shubham", 103: "Dhamma", 104: "Karan", 105: "Ashok"}

eid = int(input("Enter Employee ID: "))
if eid in dict1.keys():
    dict1.pop(eid)
    print(f"Employee ID {eid} is removed from the record ")
else:
    print(f"Employee ID {eid} is not found in the record")

print(f"Current Record is: {dict1}")