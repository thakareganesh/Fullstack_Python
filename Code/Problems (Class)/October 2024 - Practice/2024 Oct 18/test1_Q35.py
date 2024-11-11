"""
Question 35: Write a program to read meter type, last and current month electric meter reading. Now find no of units
consumed by user. Based on their bill amount. Incase meter type is residential then rs=1.49/unit otherwise 3.46/unit
"""
meter_type = input("Enter your meter type: ")
last_month_reading = int(input("Enter your last month electric meter reading: "))
current_month_reading = int(input("Enter your current month electric meter reading: "))

total_reading = current_month_reading - last_month_reading
print(total_reading,"Units consumed by user in this month")

if (meter_type == "residential" or meter_type == "RESIDENTIAL"):
    unit_charge = 1.49
    print("Unit charge per unit:",unit_charge)
    total_bill = total_reading * unit_charge
    print("Your final bill amount is:",total_bill)
else:
    unit_charge = 3.46
    print("Unit charge per unit:", unit_charge)
    total_bill = total_reading * unit_charge
    print("Your final bill amount is:", total_bill)