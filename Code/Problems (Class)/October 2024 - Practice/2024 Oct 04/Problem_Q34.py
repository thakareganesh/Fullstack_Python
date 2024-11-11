"""
Question 34: Read Market value of a land, In general stamp duty is 5%, But due to new rules it changes as 7%. So how
much extra amount they have to pay according to new rules. Calculate old stamp duty amount and new stamp duty amount
then display difference.
"""
land_value = float(input("Enter market value of the land: "))
old_stamp_percentage = 5

old_stamp_cost = land_value * old_stamp_percentage / 100
print("Old stamp duty amount:",old_stamp_cost)

new_stamp_percentage = 7
new_stamp_cost = land_value * new_stamp_percentage / 100
print("New stamp duty amount:",new_stamp_cost)

diff_of_stamp_duty = new_stamp_cost - old_stamp_cost
print("Difference between old and new stamp duty amount:",diff_of_stamp_duty)

paying_amt = land_value + new_stamp_cost
print("The final amount have to pay after new rule of stamp duty amount:",paying_amt)
