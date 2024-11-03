
"""
Question 17: Ms. Laxmi actual march milk bill is 930.0, but on that month milk boy kept 4 leaves, So
Write a program to calculate her march month milk bill
"""

mbill = 930.0
leaves = 4
days_in_march = 31

# cost_per_liter = mbill/ days_in_march
# print(cost_per_liter)

# total_bill = cost_per_liter * (days_in_march - leaves)
# print(total_bill)


# Another Way to do this

total_days = days_in_march - leaves

price_per_liter = mbill / days_in_march

total_bill = price_per_liter * total_days
print("Ms. Laxmi's March months milk bill is:",total_bill)
