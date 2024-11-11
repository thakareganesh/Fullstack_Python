# Question 2: Read EmpName then display id for that employee

dict1 = {101:"Ganesh", 102:"Shubham",103:"Dhamma",104:"Karan",105:"Ashok"}

empName = input("Enter Employee Name: ")
found = False
for id,name in dict1.items():
    if empName == name:
        print(f"Employee ID: {id}")
        found = True
        break

if not found:
    print(f"{empName} is not in the record")
    

