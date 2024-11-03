# Question 24: Consider employee monthly salary is 30000, Company reduced 12% as PF and 8% as tax. Then find monthly salary.


emp_salary = 30000 # Monthly salary

# Deductions
reduced_pf_percent = 12 # PF deduction percentage
reduced_tax_percent = 8 # Tax deduction percentage

# Calculate total deductions
total_deduction_percent = reduced_pf_percent + reduced_tax_percent

# Calculate total deduction amount
total_deduction = (emp_salary * total_deduction_percent) / 100

# Calculate final salary
final_salary = emp_salary - total_deduction
print("Final monthly salary of the employee:",final_salary)