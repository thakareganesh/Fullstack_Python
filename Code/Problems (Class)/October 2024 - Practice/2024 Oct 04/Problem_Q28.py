# Question 28: Write a program to read emp id, emp name, Gender and salary then display all details with annual salary.

emp_id = int(input("Enter Your Emp Id: "))
emp_name = input("Enter Your Name: ")
emp_gender = input("Enter Your Gender: ")
monthly_salary = float(input("Enter your monthly salary: "))

months_in_year = 12

annual_salary = monthly_salary * months_in_year

print("Employee ID is:",emp_id)
print("Employee Name is:",emp_name)
print("Employee's Gender is:", emp_gender)
print("Employee Monthly Salary is:",monthly_salary)
print("Employee Annual Salary is:", annual_salary)
