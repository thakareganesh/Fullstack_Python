# Question 2 v1: Read Medicine Name if available then print cost, read quantity from user then display billAmt


import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q = "select * from product where MedName=?"
MedName = input("Enter Medicine Name: ")
t1 = (MedName,)
cur.execute(q,t1)
data = cur.fetchall()
if data:
    if data[0][1] == MedName:
        print("Medicine Available")
        cost = data[0][2]
        print("Cost is:",cost)
        quantity = int(input("How many sheets do you want: ")) # issue 01: quantity can be more from availability
        billAmt = cost * quantity
        print("Bill Amount is:",billAmt)
else:
    print("Medicine Not Available")
con.close()