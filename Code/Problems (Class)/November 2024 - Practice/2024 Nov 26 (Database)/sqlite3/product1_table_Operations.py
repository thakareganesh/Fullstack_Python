# Product Table Question 2: Perform Operations

import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()

q1 = "select * from Product1 where pid = ?"
pid = int(input("Enter Item ID: "))
t1 = (pid,)
cur.execute(q1,t1)
data = cur.fetchall()

if data:
    if data[0][0] == pid:
        pname = data[0][1]
        cost = data[0][2]
        print(f"Your Item is: {pname}")
        print(f"{pname} Cost is: {cost}")
        quantity = int(input("Enter quantity: "))
        billAmt = cost * quantity
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