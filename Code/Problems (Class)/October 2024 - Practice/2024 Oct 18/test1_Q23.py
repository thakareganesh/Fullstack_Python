"""
Question : IRCTC allow customers to book seats, At the time of booking based on age of customer they devided into 3
types. They are 1. No ticket , 2. Half Ticket, 3. Full ticket
age less than 5 years -> No ticket
age  from 5 to 12 years and above 60 years -> Half ticket
age from 13 to 59 -> Full Tickets
"""

age = int(input("Enter your age: "))
if (age < 5):
    print("No tickets")
elif (age >= 5 and age <=12) or (age >=60):
    print("Half Tickets")
else:
    print("Full Tickets")