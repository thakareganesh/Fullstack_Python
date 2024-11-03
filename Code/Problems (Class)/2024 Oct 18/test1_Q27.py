"""
Question: Write a program to read employee salary, in-case employee monthly salary is more than or equal to 50000
then they have to pay 12% tax. Otherwise no tax.
So display monthly salary of an employee.
"""

monthly_sal = float(input("Enter employee monthly salary: "))

tax_percentage  = 0
taxAmt = 0
final_sal = monthly_sal

if monthly_sal >= 50000:
    tax_percentage = 12
    print("Tax is:", tax_percentage, "%")
    taxAmt = monthly_sal * tax_percentage / 100
    print("Tax amount is:",taxAmt)
    final_sal = monthly_sal - taxAmt
else:
    print("No Tax")

print("Actual Monthly Salary:",monthly_sal)
print("Tax Percentage       :",tax_percentage)
print("Tax Amount           :",taxAmt)
print("Final Monthly Salary :",final_sal)