"""
Question 11: Mr. Venkat deposited 500000 amount in bank for 5 years with the rate of interest as 7.8 %.
After 5 years how much amount he will receive.
(Note: Calculate interest amount and final amount, use simple interest formula)
"""

deposit = 500000
year = 5
interest_rate = 7.8

interest = deposit * interest_rate * year / 100
print("Interest earned: ", interest) # --> Output: Interest earned: 195000.0 

final_amount = interest + deposit
print("Final amount: ", final_amount) # --> Output: Final amount: 695000.0
