"""
Question 29: In RedBus
"""

tcost = int(input("Enter tickets cost: "))
no_of_tkts = int(input("How many tickets do you want: "))
coupon = input("Enter your coupon code: ")
discount = 0
bill = tcost * no_of_tkts
print("Actual Bill amount is:",bill)
if (coupon == "SAVE20"):
    discount = 20
    disAmt = bill * discount /100
    print("Your Discount is:",discount,"%")
    print("You Final Discount Amount is:",disAmt)
    finalbill = bill - disAmt
    print("Your final bill is:",finalbill)
else:
    print("Invalid Coupon, You have not get any discount")