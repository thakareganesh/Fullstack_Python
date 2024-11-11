"""
Question: In KFC website they mention an offer as up to 100rs off on bill value of 699 or more.
How to handle this case study
"""

bill_amt = float(input("Enter your bill amount: "))
if (bill_amt >= 699):
    discount = 100
    final_bill_amt = bill_amt - discount
    print("You are eligible for discount of:",discount)
    print("Final bill amount after discount:",final_bill_amt)
else:
    print("You are not eligible for a discount")
    print("Final bill amount :",bill_amt)