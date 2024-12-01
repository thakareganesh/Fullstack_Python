# Product Table Question 2: Create Table

import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
print("Connection Opened")
cur = con.cursor()
ch = "y"
while ch == "y":
    q1 = "INSERT INTO Items VALUES(?,?,?)"
    pid = int(input("Enter product id: "))
    pname = input("Enter product Name: ").title()
    cost = float(input("Enter product Cost: "))
    t1 = (pid,pname,cost)
    cur.execute(q1,t1)
    con.commit()
    ch = input("Do you want to insert more dishes for hotel menu(y/n): ").lower()
    print("Record Updated")
con.close()
print("Connection Closed")