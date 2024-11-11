month_sal = float(input("Enter your monthly Salary: "))

if (month_sal<50000):
    tax = 5
elif (month_sal>=50000 and month_sal<=100000):
    tax = 15
else:
    tax = 30

print("your tax is",tax,"%")
tax_amt = (month_sal * tax / 100)
print("your tax amount is:",tax_amt)
