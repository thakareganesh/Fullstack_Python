# Product Table Question 2: Create Table

import pyodbc as sql
con = sql.connect(driver='Sql Server', server="GANESH\\SQLEXPRESS", database='Amazon1', user='Ganesh', password='82668')
cur = con.cursor()
print("Connection Opened")
q1 = "Create table Items(ItemID int primary key,ItemName varchar(20),ItemCost money)"
cur.execute(q1)
con.commit()
print("Table Items Created")
con.close()
print("Connection Closed")