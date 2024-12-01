# question 1: read the medicine name from the user and then check available or not

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
else:
    print("Medicine Not Available")
con.close()
