"""
Question 26: Write a program to find electricity bill. Last month reading is 2234 units,
Current months reading is 2456. Now find no of units consumed, Then calculate bill amount.
Per unit 3.46 rs, Tax as 0.06 per unit, And service charge is Rs 30.
"""

last_month_reading = 2234
current_month_reading = 2456
per_unit_charge = 3.46
tax = 0.06
service_charge = 30

consumed_units = current_month_reading - last_month_reading
print("Total units consumed in current month:",consumed_units)

bill_amt = (consumed_units * per_unit_charge ) + (consumed_units * tax) + service_charge
print("Total bill amount:",bill_amt)

