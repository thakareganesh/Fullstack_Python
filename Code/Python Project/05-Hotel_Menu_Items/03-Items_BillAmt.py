# Product Table Question 2: Perform Operations

import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
print("Connections Opened")

q1 = "select * from Items where ItemID = ?"
ItemID = int(input("Enter Item ID: "))
t1 = (ItemID,)
cur.execute(q1,t1)
data = cur.fetchall()

if data:
    if data[0][0] == ItemID:
        ItemName = data[0][1]
        Cost = data[0][2]
        ItemCost = round(Cost,2)
        print(f"Your Item is: {ItemName}")
        print(f"{ItemName} Cost is: {ItemCost}")
        quantity = int(input("Enter quantity: "))
        billAmt = ItemCost * quantity
        print(f"Bill Amount is: {billAmt}")
        disc = 0
        discAmt = 0
        if billAmt > 300:
            disc = 20
            discAmt = billAmt * disc / 100
        print(f"Your Discount is: {disc}%")
        print(f"Your Discount Amount is: {discAmt}₹")
        finBillAmt = billAmt - discAmt
        cust_paid = int(input("Customer paid: "))
        if cust_paid < finBillAmt:
            print("Insufficient payment! Please pay the remaining amount.")
            remaining = finBillAmt - cust_paid
            print(f"You still owe: {remaining}₹")
        else:
            balance = cust_paid - finBillAmt
            print(f"Remaining Balance Amount is: {balance}₹")
else:
    print("Invalid Choice")
con.close()
print("Connections Closed")