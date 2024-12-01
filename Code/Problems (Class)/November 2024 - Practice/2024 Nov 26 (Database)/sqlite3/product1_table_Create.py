# Product Table Question 2: Create Table

import sqlite3 as sql
con = sql.connect('Amazon')
cur = con.cursor()
q1 = "Create table Product1(pid int primary key,pname text,cost real)"
cur.execute(q1)
con.commit()
con.close()