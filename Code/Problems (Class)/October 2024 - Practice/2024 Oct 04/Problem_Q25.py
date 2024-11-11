"""
Question 25: Mr. Venkat took 500000 loan from bank for 4 years with rate or interest as 11.4%,
Now calculate interest amount, final amount and EMI.
"""

loan = 500000
time = 4
rate_of_interest = 11.4
months_in_year = 12

emi_months = months_in_year * time
#print(emi_months)

interest_amt = loan * time * rate_of_interest / 100
print("The total interest is:", interest_amt)

final_amt = loan + interest_amt
print("The final amount is:", final_amt)

emi_amt = final_amt / emi_months
print("The EMI amount is:",emi_amt)