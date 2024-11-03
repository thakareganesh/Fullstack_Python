"""
Question 23: Consider Pizza cost is 326.50, Customer order for 3 pizzas, Now calculate bill amount.
Shop provides 20% discount on bill amount. So find the discount amount and final bill.
"""

pizza_cost = 326.50
order_quantity = 3
discount_in_percent = 20

bill_amt = pizza_cost * order_quantity
print("Orignal bill amount:", bill_amt) # --> orignal price is 979.5

discount_amt = bill_amt * discount_in_percent / 100
print("Total discount on the bill:", discount_amt) # --> discount is 195.9

final_amount = bill_amt - discount_amt
print("Final amount after discount:",final_amount) # -->  final amount is 783.6