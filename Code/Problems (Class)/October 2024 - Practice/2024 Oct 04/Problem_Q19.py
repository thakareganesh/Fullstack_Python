"""
Question 19: In an apartment they need 6 water tins per day. Write a program to calculate august month bill.
Each water tin cost is 20rs
"""

water_tins_per_day = 6
cost_of_water_tins = 20
days_in_august = 31

total_water_tins = days_in_august * water_tins_per_day
print("Total water tins in August Month:",total_water_tins)

total_bill = total_water_tins * cost_of_water_tins
print("August months bill:",total_bill)