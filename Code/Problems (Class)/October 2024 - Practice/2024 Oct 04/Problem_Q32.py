"""
# Question 32: From Hyderabad to Vijayawada General ticket cost is rs 460, Due to festival session the cost increased
as 50% (actual cost + 50% hike), now read no. of tickets and final total bill amount.
"""

ticket_cost = 460
hike = ticket_cost * 50/100
print("Actual ticket cost:",ticket_cost)

increased_ticket_cost = ticket_cost + hike
print("Increased ticket cost:",increased_ticket_cost)

ticket_quantity = int(input("How many ticket you want: "))

total_bill = ticket_quantity * increased_ticket_cost
print("Final Bill is:", total_bill)
