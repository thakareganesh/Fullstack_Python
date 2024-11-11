"""
# Question 37: Miss Pooja Mansi rent a car to go to Vijayawada, Then she started her journey from Hyderabad to Vijayawada
by car. While starting her journey she noticed that car reading as 11236. After reached Vijayawada again she noticed that
her car reading shows 11494. Now write a program to find number of kilometers she travelled. And find her bill amount.
Note: Per km they charge Rs: 15 and for total tollgate charge as Rs 200
"""

hyd_reading = 11236
vjwd_reading = 11494
per_km_charge = 15
tollgate_charge = 200

total_travel = vjwd_reading - hyd_reading
print("Miss Pooja Mansi travelled kilometers is:",total_travel)

total_bill = (total_travel * per_km_charge) + tollgate_charge
print("Miss Pooja's final bill is:",total_bill)