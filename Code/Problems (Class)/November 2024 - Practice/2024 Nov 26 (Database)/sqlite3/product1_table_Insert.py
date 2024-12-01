# Product Table Question 2: Create Table

import sqlite3 as sql
con = sql.connect('Amazon')
print("Connection Opened")
cur = con.cursor()
ch = "y"
while ch == "y":
    q1 = "INSERT INTO product1 VALUES(?,?,?)"
    pid = int(input("Enter product id: "))
    pname = input("Enter product Name: ").capitalize()
    cost = float(input("Enter product Cost: "))
    t1 = (pid,pname,cost)
    cur.execute(q1,t1)
    con.commit()
    ch = input("Do you want to insert more dishes for hotel menu(y/n): ").lower()
    print("Record Updated")
con.close()
print("Connection Closed")