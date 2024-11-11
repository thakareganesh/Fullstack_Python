"""
Question 37: Read Mango cost per kg, then read quantity. Big Basket gives offer as 22% discount on Bill Amount.
So find Total Bill Amount
"""

mango_cost = int(input("What is the Mango Price per KG: "))
quantity = float(input("How many kg of mango do you want: "))

actual_billAmt = mango_cost * quantity
print("Original bill amount without discount: ",actual_billAmt)

discount = 22
discount_Amt = actual_billAmt * discount / 100

final_billAmt = actual_billAmt - discount_Amt
print("Final bill amount after 22 % Discount:",final_billAmt)
