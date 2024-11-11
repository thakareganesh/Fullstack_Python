"""
Question 28:
"""

pcost = float(input("Enter your product cost       : "))
quantity = int(input("How many products do you want: "))
card = input("Enter your card Name: ")
discount = 0
finalBill = pcost * quantity
if (card == "ICICI"):
    discount = 15
    disAmt = pcost * discount / 100
    finalBill = finalBill - disAmt
else:
    print("Not applicable for any discount")

print("Product cost:",pcost)
print("Quntity:",quantity)
print("Discount",discount)
print("Final Bill:",finalBill)