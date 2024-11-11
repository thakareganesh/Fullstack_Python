# Problem 1:

# taking input from user
product_cost = int(input("Enter Product Cost: "))
quantity = int(input("Enter quantity: "))
card = input("Enter your card name: ")

# initialize discount and discount amount as Zero for handling post error
dis = 0
disAmt = 0

# calculating bill
billAmt = product_cost * quantity

# discount logic
if (billAmt > 5000 or card=="city"):
    dis = 20
    disAmt = billAmt * dis / 100
# final bill
finalBill = billAmt - disAmt

print("Actual Bill is:",billAmt)
print("Discount you got:",dis,"%")
print("Discount Amount:",disAmt)
print("Final bill Amount:",finalBill)