"""
# Task 4: Consider Emp Email ID's are ["venkat@ibm.com","vishnu@tcs.com","ganesh@wipro.com","harshu@ibm.com"]
# Test Case 1: Enter your Company Name: ibm
               Your Employees are: venkat   harshu
"""
emp_emails = ["venkat@ibm.com","vishnu@tcs.com","ganesh@wipro.com","harshu@ibm.com"]
company_name = input("Enter your compony Name: ").lower()
found_employees = []

for email in emp_emails:
    employees = email.split("@")
    found_employees.append(employees)

# print(found_employees)
print("Your Employees are: ",end="")
for emp in found_employees:
    if emp[1].startswith(company_name):
        print(emp[0], end="\t")