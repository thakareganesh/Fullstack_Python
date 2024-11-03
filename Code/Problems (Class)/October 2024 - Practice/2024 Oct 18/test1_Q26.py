"""
Question: Write a program to read product cost, quantity then find bill amount. In case bill amount crossed 5000 then
provide 20 % discount on bill amount, then display Bill amount, Discount, Discount Amount, and final bill.
"""
pcost = int(input("Enter product cost: "))
quantity = int(input("How many products do you want: "))

billAmt = pcost * quantity

disc = 0
discAmt = 0
final_billAmt = billAmt 

if (billAmt > 5000):
    disc = 20
    discAmt = billAmt * disc / 100
    final_billAmt = billAmt - discAmt
print("Actual Bill Amount:",billAmt)
print("Discount          :",disc,"%")
print("Discount Amount   :",discAmt)
print("Final Bill Amount :",final_billAmt)


